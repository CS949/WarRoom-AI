<script setup>
import { useI18n } from "vue-i18n";

const { locale } = useI18n();

const changeLanguage = (event) => {

  locale.value = event.target.value;

  localStorage.setItem(
    "language",
    event.target.value
  );
};
</script>

<template>

<select
  :value="locale"
  @change="changeLanguage"
  class="px-3 py-2 rounded-lg border dark:bg-slate-800"
>
  <option value="en">
    🇺🇸 English
  </option>

  <option value="zh">
    🇨🇳 中文
  </option>

  <option value="hi">
    🇮🇳 हिन्दी
  </option>

  <option value="es">
    🇪🇸 Español
  </option>

  <option value="ar">
    🇸🇦 العربية
  </option>

  <option value="fr">
    🇫🇷 Français
  </option>

  <option value="ru">
    🇷🇺 Русский
  </option>

  <option value="ja">
    🇯🇵 日本語
  </option>

  <option value="de">
    🇩🇪 Deutsch
  </option>
</select>

</template>