# سجل التغييرات التاريخي (CHANGELOG)

## [2026-08-28] - إصلاح وتكوين build.gradle لبوابة الأندرويد
- **المهمة**: تصحيح إعدادات البناء لـ `android-gateway/build.gradle` ودعم `assembleDebug`.
- **الملفات المتأثرة**: `android-gateway/build.gradle`, `docs/ai/CURRENT_STATE.md`, `docs/ai/CHANGELOG.md`.
- **التغيير**:
  - إضافة `buildscript` وإعداد مستودعات `google()` و `jcenter()`.
  - تطبيق `com.android.application` وتحديد `compileSdkVersion 23` و `minSdkVersion 23` و `targetSdkVersion 23`.
  - إضافة مستودع JitPack والاعتماديات لـ OkHttp و LiveKit SDK.

## [2026-08-28] - تحديث عنوان IP السيرفر في بوابة الأندرويد
- **المهمة**: تعديل عناوين الاتصال لـ n8n و LiveKit في تطبيق الأندرويد لاستخدام `192.168.1.103`.
- **الملفات المتأثرة**: `android-gateway/src/main/java/com/awsan/gateway/CallReceiver.java`, `android-gateway/src/main/java/com/awsan/gateway/LiveKitBridgeService.java`, `docs/ai/CURRENT_STATE.md`, `docs/ai/CHANGELOG.md`.
- **التغيير**:
  - استبدال عنوان IP القديم `192.168.1.50` بـ `192.168.1.103` لروابط الـ Webhooks لـ n8n وخادم LiveKit.
  - تحديث الذاكرة الدائمة وحالة المشروع.

## [2026-08-28] - تشغيل الحاويات وتأكيد حالة الخدمات
- **المهمة**: تشغيل الخدمات عبر `docker compose up -d --build` والتحقق من سلامة البيئة التشغيلية.
- **الملفات المتأثرة**: `docs/ai/CURRENT_STATE.md`, `docs/ai/CHANGELOG.md`.
- **التغيير**:
  - التأكد من تشغيل حاويات n8n و LiveKit بنجاح بدون أخطاء باستعمال `docker compose v2`.
  - تحديث الذاكرة الدائمة وسجل الحالة الحالية لتعكس نجاح عملية التشغيل.

## [2026-08-28] - إصلاح وتحديث إعدادات Docker Compose v2
- **المهمة**: تصحيح إعدادات Docker والمنافذ وحل خطأ توافقية الإصدارات القديمة.
- **الملفات المتأثرة**: `docker-compose.yml`, `docs/ai/CURRENT_STATE.md`, `docs/ai/CHANGELOG.md`.
- **التغيير**:
  - إزالة الخاصية المتروكة `version` من `docker-compose.yml` للتوافق مع معايير `docker compose v2`.
  - التأكد من سلامة تكوين المنافذ لـ LiveKit و n8n بدون أي تعارض.
  - تحديث الذاكرة الدائمة وسجل التغييرات ليعكس التحديث المعماري للبيئة.

## [2026-08-28] - توحيد واجهة المستخدم وإدراج الهوية الجديدة
- **المهمة**: تنفيذ توحيد واجهة المستخدم (UI Unification) وتحديث ذاكرة المشروع.
- **الملفات المتأثرة**: `public/index.html`, `docs/ai/CURRENT_STATE.md`, `docs/ai/FEATURES.md`, `docs/ai/PROJECT_MAP.md`, `docs/ai/CHANGELOG.md`.
- **التغيير**:
  - اعتماد اسم العلامة التجارية **AwsanBot** والشعار الموحد في الواجهة `public/index.html`.
  - توحيد لوحة التحكم لمراقبة خادم LiveKit ومحرك الأتمتة n8n وسجل المواعيد.
  - تحديث وثائق الذاكرة الدائمة لتعكس اكتمال الميزة.

## [2026-08-28] - إضافة الوكيل الصوتي وتأطير الذاكرة الدائمة
- **المهمة**: إنشاء الوكيل الصوتي العربي وتوثيق كامل الذاكرة الدائمة للمشروع.
- **الملفات المتأثرة**: `AGENTS.md`, `agent.py`, وكافة ملفات `docs/ai/`.
- **التغيير**:
  - التأكد من سلامة المنافذ وعدم التعارض في `docker-compose.yml`.
  - إنشاء ملف `agent.py` للربط بين LiveKit و OpenAI و n8n Webhook.
  - إرسال الالتزام البرمجي بـ git hash `01ce39d`.
  - تحديث وتأطير كافة ملفات الذاكرة الدائمة لمشروع AwsanBot وفق معايير الجودة الإلزامية.

## [2026-08-28] - إعداد البنية التأسيسية
- **المهمة**: إنشاء المستودع وتجهيز نظام الذاكرة الدائمة وتشغيل الحاويات.
- **الملفات المتأثرة**: `docker-compose.yml` وملفات التوثيق الأولية.
- **التغيير**: تأسيس الهيكل التكاملي لمشروع AwsanBot وصياغة قواعد العمل.
