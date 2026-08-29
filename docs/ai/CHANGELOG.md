# سجل التغييرات التاريخي (CHANGELOG)

## [2026-08-28] - تحديث مسار عمل GitHub Actions وتثبيت نظام الذاكرة الدائمة
- **المهمة**: تحديث `.github/workflows/build-apk.yml` وإنشاء/تثبيت ملفات الذاكرة الدائمة في `docs/ai/`.
- **الملفات المتأثرة**: `.github/workflows/build-apk.yml`, كافة ملفات `docs/ai/`.
- **التغيير**:
  - ضبط صلاحيات `gradlew` ومسار بناء الـ APK في GitHub Actions.
  - إعداد وتوثيق ملفات الذاكرة الدائمة (`PROJECT.md`, `CURRENT_STATE.md`, `PROJECT_MAP.md`, `ARCHITECTURE.md`, `FEATURES.md`, `DECISIONS.md`, `CHANGELOG.md`, `FORK_STRATEGY.md`, `MEMORY_RULES.md`).
