vue
<script setup>

import { ref } from "vue";
import axios from "axios";
import MarkdownIt from "markdown-it";

import Navbar from "../components/Navbar.vue";
import Footer from "../components/Footer.vue";

const md = new MarkdownIt({
  html: true,
  linkify: true,
  breaks: true
});

const decision = ref("");

const loading = ref(false);

const agents = ref([]);

const moderator = ref("");

const consensusScore = ref(null);

const conflictScore = ref(null);

const startVoiceInput = () => {

  const SpeechRecognition =
    window.SpeechRecognition ||
    window.webkitSpeechRecognition;

  if (!SpeechRecognition) {

    alert(
      "Speech recognition is not supported."
    );

    return;
  }

  const recognition =
    new SpeechRecognition();

  recognition.lang = "en-US";

  recognition.continuous = false;

  recognition.interimResults = false;

  recognition.onresult = (event) => {

    decision.value =
      event.results[0][0].transcript;

  };

  recognition.start();

};

const analyzeDecision = async () => {

  if (!decision.value.trim()) {

    alert(
      "Please enter a decision."
    );

    return;

  }

  try {

    loading.value = true;

    const response =
      await axios.post(

        `${import.meta.env.VITE_API_URL}/api/analyze`,

        {
          decision: decision.value
        }

      );

    const data = response.data;

    agents.value =
      Object.entries(
        data.agents
      );

    moderator.value =
      data.moderator;

    consensusScore.value =
      data.consensus_score;

    conflictScore.value =
      data.conflict_score;

  }

  catch(error){

    console.log(error);

    alert(
      "Backend connection failed."
    );

  }

  finally{

    loading.value = false;

  }

};

const renderMarkdown = (text) => {

  return md.render(
    text || ""
  );

};

const getAgentDetails = (name) => {

const details = {

"CEO Agent":{

icon:"👔",

color:"bg-indigo-600"

},

"CFO Agent":{

icon:"💰",

color:"bg-emerald-600"

},

"CTO Agent":{

icon:"⚙️",

color:"bg-cyan-600"

},

"Marketing Agent":{

icon:"📈",

color:"bg-orange-600"

},

"Legal Agent":{

icon:"⚖️",

color:"bg-purple-600"

},

"Risk Agent":{

icon:"🚨",

color:"bg-red-600"

}

};

return details[name] || {

icon:"🤖",

color:"bg-slate-600"

};

};

</script>

<template>

<div

id="main-content"

class="min-h-screen bg-slate-100 dark:bg-slate-950 dark:text-white">

<Navbar />

<section
class="max-w-7xl mx-auto px-4 py-10">

<div
class="text-center">

<h1
class="text-5xl font-bold">

WARROOM AI

</h1>

<p
class="mt-4 text-slate-500 max-w-4xl mx-auto">

An AI Decision Intelligence Platform that helps businesses, NGOs, governments and communities make transparent, evidence-based decisions.

</p>

<div
class="flex flex-wrap justify-center gap-3 mt-6">

<span class="bg-blue-100 text-blue-700 px-4 py-2 rounded-full font-semibold">

🧠 Multi-Agent Reasoning

</span>

<span class="bg-purple-100 text-purple-700 px-4 py-2 rounded-full font-semibold">

💡 Microsoft Foundry IQ

</span>

<span class="bg-green-100 text-green-700 px-4 py-2 rounded-full font-semibold">

♿ Accessibility First

</span>

<span class="bg-orange-100 text-orange-700 px-4 py-2 rounded-full font-semibold">

☁️ Azure Powered

</span>

<span class="bg-pink-100 text-pink-700 px-4 py-2 rounded-full font-semibold">

🌍 Social Impact Ready

</span>

</div>

</div>

</section>

<section
class="max-w-5xl mx-auto px-4 pb-10">

<div
class="bg-white dark:bg-slate-900 rounded-3xl shadow-xl p-8">

<h2
class="text-3xl font-bold mb-6">

AI Decision Intelligence Workspace

</h2>

<div
class="relative">

<textarea

aria-label="Decision Input"

spellcheck="true"

v-model="decision"

rows="6"

placeholder="Example: Should we launch EV charging stations in rural Japan?"

class="w-full rounded-2xl border border-slate-300 dark:border-slate-700 dark:bg-slate-800 p-5 pr-20 resize-none focus:outline-none focus:ring-2 focus:ring-blue-500"

></textarea>

<button

@click="startVoiceInput"

aria-label="Start Voice Input"

title="Voice Input"

class="absolute bottom-4 right-4 flex items-center justify-center w-12 h-12 rounded-full bg-gradient-to-r from-blue-600 to-purple-600 hover:scale-110 transition duration-300 shadow-lg"

>

<svg

xmlns="http://www.w3.org/2000/svg"

fill="none"

viewBox="0 0 24 24"

stroke-width="1.8"

stroke="currentColor"

class="w-6 h-6 text-white"

>

<path

stroke-linecap="round"

stroke-linejoin="round"

d="M12 18.75a6.75 6.75 0 006.75-6.75V8.25a.75.75 0 00-1.5 0V12a5.25 5.25 0 11-10.5 0V8.25a.75.75 0 00-1.5 0V12A6.75 6.75 0 0012 18.75zm0 0v3m-3-3h6"

/>

</svg>

</button>

</div>

<button

@click="analyzeDecision"

aria-label="Analyze Decision"

class="w-full mt-6 py-4 rounded-2xl bg-blue-600 hover:bg-blue-700 text-white font-semibold text-lg"

>

{{ loading ? "⚡ Executive Agents Debating..." : "Start Executive Debate" }}

</button>

<div

v-if="loading"

class="mt-6 text-center"

>

<div

class="text-lg font-semibold"

>

🤖 Executive Reasoning Agents are discussing...

</div>

<div

class="mt-3 text-slate-500"

>

👔 CEO

💰 CFO

⚙️ CTO

📈 Marketing

⚖️ Legal

🚨 Risk

</div>

</div>

</div>

</section>

<section

v-if="consensusScore !== null"

class="max-w-7xl mx-auto px-4 pb-10"

>

<div

class="grid md:grid-cols-2 gap-6"

>

<div

class="bg-green-100 dark:bg-green-200 rounded-3xl shadow-lg p-8 text-center text-slate-900"

>

<div class="text-5xl">

🤝

</div>

<h3

class="font-bold text-3xl mt-3"

>

Consensus

</h3>

<p

class="text-6xl font-bold text-green-700 mt-4"

>

{{ consensusScore }}%

</p>

<p

class="mt-4 text-lg"

>

Strong Agreement

</p>

</div>

<div

class="bg-pink-100 dark:bg-pink-200 rounded-3xl shadow-lg p-8 text-center text-slate-900"

>

<div class="text-5xl">

⚔️

</div>

<h3

class="font-bold text-3xl mt-3"

>

Conflict

</h3>

<p

class="text-6xl font-bold text-pink-700 mt-4"

>

{{ conflictScore }}%

</p>

<p

class="mt-4 text-lg"

>

Healthy Debate

</p>

</div>

</div>

</section>

<section

v-if="agents.length"

class="max-w-7xl mx-auto px-4 pb-10"

>

<h2

class="text-4xl font-bold text-center mb-10"

>

Executive Reasoning Agents

</h2>

<div

class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-8"

>

<div

v-for="[name, result] in agents"

:key="name"

class="bg-white dark:bg-slate-900 rounded-3xl shadow-xl overflow-hidden"

>

<div

:class="[

getAgentDetails(name).color,

'text-white p-5 text-xl font-bold'

]"

>

{{ getAgentDetails(name).icon }}

{{ name }}

</div>

<div

class="p-6"

>

<div

class="prose dark:prose-invert max-w-none"

v-html="renderMarkdown(result)"

></div>

</div>

</div>

</div>

</section>

<section

v-if="moderator"

class="max-w-7xl mx-auto px-4 pb-20"

>

<div

class="bg-white dark:bg-slate-900 rounded-3xl shadow-xl overflow-hidden"

>

<div

class="bg-purple-600 text-white p-5 text-2xl font-bold"

>

🏛️ Board Moderator Recommendation

</div>

<div

class="p-8"

>

<div

class="prose dark:prose-invert max-w-none"

v-html="renderMarkdown(moderator)"

></div>

</div>

</div>

</section>

<Footer />

</div>

</template>

