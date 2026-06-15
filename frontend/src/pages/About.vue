<script setup>
import Navbar from "../components/Navbar.vue";
import Footer from "../components/Footer.vue";
</script>

<template>

  <div
    class="min-h-screen bg-white dark:bg-slate-950 dark:text-white"
  >

    <Navbar />

    <section
      class="max-w-5xl mx-auto px-4 py-16"
    >

      <h1
        class="text-5xl font-bold mb-10"
      >
        About WarRoom AI
      </h1>

      <div class="space-y-10">

        <div>

          <h2 class="text-2xl font-bold mb-3">
            Project Overview
          </h2>

          <p class="leading-8">
            WarRoom AI is a Multi-Agent Decision Intelligence Platform that helps users make strategic decisions through collaborative AI reasoning, contradiction analysis, and evidence-based recommendations.
          </p>

        </div>

        <div>

          <h2 class="text-2xl font-bold mb-3">
            Vision
          </h2>

          <p class="leading-8">
            To make strategic decision-making transparent, explainable, accessible, and multilingual for businesses, NGOs, educators, healthcare organizations, and individuals.
          </p>

        </div>

        <div>

          <h2 class="text-2xl font-bold mb-3">
            Creator
          </h2>

          <p class="leading-8">
            Chaitanya Sunil Sharma
            <br>
            Information Technology Engineer
            <br>
            Community Builder & AI Enthusiast
          </p>

        </div>

        <div>

          <h2 class="text-2xl font-bold mb-3">
            Technology Stack
          </h2>

          <ul class="space-y-2">
            <li>Vue.js 3</li>
            <li>Tailwind CSS</li>
            <li>Python Flask</li>
            <li>GitHub Models</li>
            <li>Microsoft Foundry IQ</li>
            <li>Azure Cosmos DB (MongoDB)</li>
            <li>Browser Speech Recognition API</li>
            <li>Microsoft Azure</li>
          </ul>

        </div>

      </div>

    </section>

    <Footer />

  </div>

</template>