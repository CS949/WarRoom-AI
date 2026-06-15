<script setup>

import { ref } from "vue";
import { RouterLink } from "vue-router";

import ThemeToggle from "./ThemeToggle.vue";
// import LanguageSelector from "./LanguageSelector.vue";

import { useI18n } from "vue-i18n";

const { t } = useI18n();

const mobileMenu = ref(false);

const closeMenu = () => {

mobileMenu.value = false;

};

</script>

<template>

<nav

aria-label="Primary Navigation"

class="bg-slate-950 border-b border-slate-800 sticky top-0 z-50"

>

<a

href="#main-content"

class="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 bg-blue-600 text-white px-4 py-2 rounded-lg z-50"

>

Skip to main content

</a>

<div

class="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between"

>

<RouterLink
  to="/"
  class="flex items-center gap-3"
>

<img

src="/WarRoom-AI_Favicon.svg"

alt="WarRoom AI Logo"

class="h-12 w-auto"

>

<span

class="text-2xl font-bold text-white"

>

WarRoom AI

</span>

</RouterLink>

<div

class="hidden md:flex items-center gap-6"

>

<RouterLink

to="/"

class="text-white hover:text-blue-500 transition"

>

{{ t("home") }}

</RouterLink>

<RouterLink

to="/history"

class="text-white hover:text-blue-500 transition"

>

History

</RouterLink>

<RouterLink

to="/about"

class="text-white hover:text-blue-500 transition"

>

{{ t("about") }}

</RouterLink>

<!-- <LanguageSelector /> -->

<ThemeToggle />

</div>

<button

@click="mobileMenu=!mobileMenu"

aria-label="Toggle Mobile Menu"

class="md:hidden text-white text-3xl"

>

{{ mobileMenu ? "✕" : "☰" }}

</button>

</div>

<transition

enter-active-class="transition duration-200"

leave-active-class="transition duration-200"

>

<div

v-if="mobileMenu"

class="md:hidden border-t border-slate-800 bg-slate-950"

>

<div

class="flex flex-col gap-4 p-4"

>

<RouterLink

to="/"

@click="closeMenu"

class="text-white"

>

{{ t("home") }}

</RouterLink>

<RouterLink

to="/history"

@click="closeMenu"

class="text-white"

>

History

</RouterLink>

<RouterLink

to="/about"

@click="closeMenu"

class="text-white"

>

{{ t("about") }}

</RouterLink>

<!-- <LanguageSelector /> -->

<ThemeToggle />

</div>

</div>

</transition>

</nav>

</template>