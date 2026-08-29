# سجل التغييرات التاريخي (CHANGELOG)

## [2026-08-28] - تحديث وتطوير سير العمل في GitHub Actions
- **المهمة**: تحديث ملف `.github/workflows/build-apk.yml` بالنسخ الأحدث لـ checkout و setup-java وضبط اسم الـ artifact.
- **الملفات المتأثرة**: `.github/workflows/build-apk.yml`, `docs/ai/CURRENT_STATE.md`, `docs/ai/CHANGELOG.md`.
- **التغيير**:
  - ترقية `actions/checkout` إلى الإصدار v4.
  - ترقية `actions/setup-java` إلى الإصدار v4 وتثبيت توزيعة temurin لجافا 17.
  - توحيد اسم الأرتفكت المرفوع ليكون `app-debug`.
  - تحديث نظام الذاكرة الدائمة للمشروع.

## [2026-08-28] - تحديث مسار عمل GitHub Actions وتثبيت نظام الذاكرة الدائمة
- **المهمة**: تحديث `.github/workflows/build-apk.yml` وإنشاء/تثبيت ملفات الذاكرة الدائمة في `docs/ai/`.
- **الملفات المتأثرة**: `.github/workflows/build-apk.yml`, كافة ملفات `docs/ai/`.
- **التغيير**:
  - ضبط صلاحيات `gradlew` ومسار بناء الـ APK في GitHub Actions.
  - إعداد وتوثيق ملفات الذاكرة الدائمة (`PROJECT.md`, `CURRENT_STATE.md`, `PROJECT_MAP.md`, `ARCHITECTURE.md`, `FEATURES.md`, `DECISIONS.md`, `CHANGELOG.md`, `FORK_STRATEGY.md`, `MEMORY_RULES.md`).
