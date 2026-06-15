import { createI18n } from "vue-i18n";

import en from "./locales/en.json";
import hi from "./locales/hi.json";
import zh from "./locales/zh.json";
import es from "./locales/es.json";
import ar from "./locales/ar.json";
import fr from "./locales/fr.json";
import ru from "./locales/ru.json";
import ja from "./locales/ja.json";
import de from "./locales/de.json";

const savedLanguage =
  localStorage.getItem("language") || "en";

const i18n = createI18n({
  legacy: false,
  locale: savedLanguage,
  fallbackLocale: "en",
  messages: {
    en,
    hi,
    zh,
    es,
    ar,
    fr,
    ru,
    ja,
    de
  }
});

export default i18n;