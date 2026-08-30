# سجل التغييرات التاريخي (CHANGELOG)

## [2026-08-28] - إنشاء settings.gradle وتحديث build.gradle لإصدار AGP 4.1.0
- **المهمة**: إضافة ملف إعدادات Gradle لبوابة الأندرويد وتضمين buildscript dependencies.
- **الملفات المتأثرة**: `android-gateway/settings.gradle`, `android-gateway/build.gradle`, `docs/ai/CURRENT_STATE.md`, `docs/ai/CHANGELOG.md`.
- **التغيير**:
  - إنشاء `android-gateway/settings.gradle` بالاسم `rootProject.name = "android-gateway"`.
  - تحديث `android-gateway/build.gradle` لإضافة `buildscript` مع `com.android.tools.build:gradle:4.1.0`.
  - تحديث نظام الذاكرة الدائمة للمشروع.

## [2026-08-28] - إنشاء بيان الأندرويد وتحسين مسارات البناء والتخزين المؤقت
- **المهمة**: إضافة `AndroidManifest.xml` وتحديث `build.gradle` ومسار مخرجات الأرتفكت في `build-apk.yml`.
- **الملفات المتأثرة**: `android-gateway/src/main/AndroidManifest.xml`, `android-gateway/build.gradle`, `.github/workflows/build-apk.yml`, `docs/ai/CURRENT_STATE.md`, `docs/ai/CHANGELOG.md`.
- **التغيير**:
  - إنشاء ملف `AndroidManifest.xml` المتوافق مع الصلاحيات المطلوبة (`READ_PHONE_STATE`, `PROCESS_OUTGOING_CALLS`, `INTERNET`).
  - تحديث `build.gradle` لإضافة مستودع `mavenCentral` وتبعيات OkHttp و Annotations.
  - تعديل مسار رفع الأرتفكت في GitHub Actions إلى `android-gateway/build/outputs/apk/debug/*.apk`.
  - تحديث الذاكرة الدائمة للمشروع.

## [2026-08-28] - تحديث سير العمل لاستخدام JDK 11 لضمان توافق Gradle 6.5
- **المهمة**: تحديث `.github/workflows/build-apk.yml` لضبط إصدار Java إلى 11 وإضافة خطوة التحقق من إصدار Gradle.
- **الملفات المتأثرة**: `.github/workflows/build-apk.yml`, `docs/ai/CURRENT_STATE.md`, `docs/ai/CHANGELOG.md`.
- **التغيير**:
  - ضبط setup-java على JDK 11 (temurin) لدعم Gradle 6.5.
  - إضافة خطوة `./gradlew --version` للتحقق من التوافق قبل البناء.
  - تحديث الذاكرة الدائمة للمشروع.
