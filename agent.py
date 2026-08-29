import asyncio
import logging
import aiohttp
from livekit.agents import (
    AutoSubscribe,
    JobContext,
    WorkerOptions,
    cli,
    llm,
)
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import openai, silero

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("voice-agent")

N8N_WEBHOOK_URL = "http://localhost:5678/webhook/manage-appointment"


class AssistantFunction(llm.FunctionContext):
    """
    مجموعة الأدوات/الدوال التي يمكن للمساعد الذكي استخدامها للربط مع n8n
    """

    @llm.ai_callable(
        description="إرسال طلب إلى n8n لحجز أو إدارة موعد أو إرسال رسالة"
    )
    async def send_to_n8n(
        self,
        action: str = llm.TypeInfo(description="نوع الإجراء: 'book_appointment' أو 'send_message'"),
        name: str = llm.TypeInfo(description="اسم المستخدم أو العميل"),
        details: str = llm.TypeInfo(description="تفاصيل الموعد أو نص الرسالة"),
    ) -> str:
        """ترسل البيانات إلى n8n Webhook"""
        payload = {
            "action": action,
            "name": name,
            "details": details,
        }
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(N8N_WEBHOOK_URL, json=payload) as resp:
                    if resp.status == 200:
                        return "تم إرسال الطلب بنجاح إلى n8n وتمت معالجته."
                    else:
                        return f"تم إرسال الطلب ولكن استجابت n8n برمز الحالة: {resp.status}"
        except Exception as e:
            logger.error(f"خطأ أثناء الاتصال بـ n8n: {e}")
            return "حدث خطأ أثناء محاولة الاتصال بنظام إدارة المواعيد (n8n)."


async def entrypoint(ctx: JobContext):
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    # إعداد سياق الدوال (Tools)
    fnc_ctx = AssistantFunction()

    # إنشاء المساعد الصوتي وتحديد التعليمات باللغة العربية
    assistant = VoiceAssistant(
        vad=silero.VAD.load(),
        stt=openai.STT(language="ar"),
        llm=openai.LLM(model="gpt-4o-mini"),
        tts=openai.TTS(voice="alloy"),
        fnc_ctx=fnc_ctx,
    )

    # بدء المساعد الصوتي في الغرفة
    assistant.start(ctx.room)

    # رسالة ترحيبية باللغة العربية
    await assistant.say("أهلاً بك! أنا مساعدك الذكي. كيف يمكنني مساعدتك اليوم في حجز المواعيد أو إرسال الرسائل؟", allow_interruptions=True)


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
