<script setup>
import { ref, onMounted } from "vue";

const darkMode = ref(true);

onMounted(() => {
  const savedTheme =
    localStorage.getItem("theme");

  if (savedTheme === "light") {
    darkMode.value = false;
    document.documentElement.classList.remove("dark");
  } else {
    darkMode.value = true;
    document.documentElement.classList.add("dark");
  }
});

const toggleTheme = () => {

  darkMode.value = !darkMode.value;

  if (darkMode.value) {

    document.documentElement.classList.add("dark");

    localStorage.setItem(
      "theme",
      "dark"
    );

  } else {

    document.documentElement.classList.remove("dark");

    localStorage.setItem(
      "theme",
      "light"
    );

  }
};
</script>

<template>

  <button
    @click="toggleTheme"
    class="px-3 py-2 rounded-lg bg-slate-700 hover:bg-slate-600 text-white transition"
  >
    {{ darkMode ? "🌙" : "☀️" }}
  </button>

</template>