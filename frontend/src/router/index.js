import { createRouter, createWebHistory } from "vue-router";

import Home from "../pages/Home.vue";
import About from "../pages/About.vue";
import History from "../pages/History.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    component: About,
  },
  {
  path: "/history",
  name: "history",
  component: History
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;