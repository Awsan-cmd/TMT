# المعمارية الشبكية والبروتوكولات (Architecture)

## مخطط الاتصالات والبروتوكولات
- **اتصال المكالمات**: الهاتف المحمول (Android Gateway) يلتقط حالة المكالمة ويرسل Webhook إلى n8n (`192.168.1.103:5678`) ويشغل `LiveKitBridgeService`.
- **الصوت الذكي**: `agent.py` يربط جلسات LiveKit مع محرك OpenAI STT/TTS/LLM، ويتواصل مع n8n عبر Webhooks (`/webhook/manage-appointment`) لإدارة المواعيد.
- **الأتمتة**: n8n يدير سير العمل وربط الخدمات السحابية (Google Calendar, Sheets, Contacts).
