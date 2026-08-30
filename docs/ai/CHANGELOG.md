# سجل التغييرات التاريخي (CHANGELOG)

## [2026-08-28] - تحديث سير العمل لاستخدام JDK 11 لضمان توافق Gradle 6.5
- **المهمة**: تحديث `.github/workflows/build-apk.yml` لضبط إصدار Java إلى 11 وإضافة خطوة التحقق من إصدار Gradle.
- **الملفات المتأثرة**: `.github/workflows/build-apk.yml`, `docs/ai/CURRENT_STATE.md`, `docs/ai/CHANGELOG.md`.
- **التغيير**:
  - ضبط setup-java على JDK 11 (temurin) لدعم Gradle 6.5.
  - إضافة خطوة `./gradlew --version` للتحقق من التوافق قبل البناء.
  - تحديث الذاكرة الدائمة للمشروع.

## [2026-08-28] - فحص شامل وتحسين استقرار المشروع (Codebase Review & Optimization)
- **المهمة**: إجراء فحص شامل لكافة ملفات الكود والبناء، وإصلاح خطأ سكريبت `gradlew.bat`.
- **الملفات المتأثرة**: `android-gateway/gradlew.bat`, `docs/ai/CURRENT_STATE.md`, `docs/ai/CHANGELOG.md`.
- **التغيير**:
  - تصحيح استدعاء `jobEnd` غير المكتمل في ملف `android-gateway/gradlew.bat` إلى `goto globalEnd`.
  - التحقق من سلامة تكوينات GitHub Actions (`build-apk.yml`) ومكتبات المشروع.
  - تحديث الذاكرة الدائمة للمشروع.

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
