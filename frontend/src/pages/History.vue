<script setup>

import {

ref,

onMounted,

computed

}

from "vue";

import axios from "axios";

import Navbar from "../components/Navbar.vue";

import Footer from "../components/Footer.vue";

const history = ref([]);

const loadHistory = async () => {

try{

const response = await axios.get(

`${import.meta.env.VITE_API_URL}/api/history`

);

history.value = response.data;

}

catch(error){

console.log(error);

}

};

onMounted(() => {

loadHistory();

});

const totalDecisions = computed(() => {

return history.value.length;

});

const averageConsensus = computed(() => {

if(!history.value.length){

return 0;

}

const total = history.value.reduce(

(sum,item)=>

sum + item.consensus_score,

0

);

return Math.round(

total/history.value.length

);

});

const averageConflict = computed(() => {

if(!history.value.length){

return 0;

}

const total = history.value.reduce(

(sum,item)=>

sum + item.conflict_score,

0

);

return Math.round(

total/history.value.length

);

});

const latestDecision = computed(() => {

if(!history.value.length){

return "No decisions yet";

}

return history.value[0].decision;

});

</script>

<template>

<div

class="min-h-screen bg-slate-100 dark:bg-slate-950 dark:text-white"

>

<Navbar />

<section

class="max-w-7xl mx-auto px-4 py-10"

>

<h1

class="text-5xl font-bold text-center"

>

Executive Analytics

</h1>

<p

class="text-center text-slate-500 mt-4"

>

Historical insights from previous AI boardroom discussions

</p>

</section>

<section

class="max-w-7xl mx-auto px-4 pb-10"

>

<div

class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6"

>

<div

class="bg-blue-100 dark:bg-blue-200 text-slate-900 rounded-3xl shadow-lg p-8 text-center"

>

<div class="text-5xl">

📊

</div>

<h3

class="font-bold text-2xl mt-3"

>

Total Decisions

</h3>

<p

class="text-5xl font-bold mt-4"

>

{{ totalDecisions }}

</p>

</div>

<div

class="bg-green-100 dark:bg-green-200 text-slate-900 rounded-3xl shadow-lg p-8 text-center"

>

<div class="text-5xl">

🤝

</div>

<h3

class="font-bold text-2xl mt-3"

>

Avg Consensus

</h3>

<p

class="text-5xl font-bold text-green-700 mt-4"

>

{{ averageConsensus }}%

</p>

</div>

<div

class="bg-pink-100 dark:bg-pink-200 text-slate-900 rounded-3xl shadow-lg p-8 text-center"

>

<div class="text-5xl">

⚔️

</div>

<h3

class="font-bold text-2xl mt-3"

>

Avg Conflict

</h3>

<p

class="text-5xl font-bold text-pink-700 mt-4"

>

{{ averageConflict }}%

</p>

</div>

<div

class="bg-purple-100 dark:bg-purple-200 text-slate-900 rounded-3xl shadow-lg p-8"

>

<div class="text-5xl">

📝

</div>

<h3

class="font-bold text-2xl mt-3"

>

Latest Decision

</h3>

<p

class="mt-4"

>

{{ latestDecision }}

</p>

</div>

</div>

</section>

<section

class="max-w-7xl mx-auto px-4 pb-20"

>

<h2

class="text-4xl font-bold mb-8"

>

Decision History

</h2>

<div

v-if="!history.length"

class="bg-white dark:bg-slate-900 rounded-3xl shadow-xl p-8 text-center"

>

No decisions yet.

</div>

<div

v-for="(item,index) in history"

:key="index"

class="bg-white dark:bg-slate-900 rounded-3xl shadow-xl p-8 mb-6"

>

<h3

class="font-bold text-2xl"

>

🧠

{{ item.decision }}

</h3>

<div

class="mt-6 flex flex-wrap gap-4"

>

<div

class="bg-green-100 text-slate-900 px-5 py-3 rounded-2xl"

>

🤝 Consensus

{{ item.consensus_score }}%

</div>

<div

class="bg-pink-100 text-slate-900 px-5 py-3 rounded-2xl"

>

⚔️ Conflict

{{ item.conflict_score }}%

</div>

</div>

</div>

</section>

<Footer />

</div>

</template>