import { createRouter, createWebHistory } from 'vue-router';
import visualization from '../components/visualization-of-state.vue';

const routes = [
  {
    path: '/',
    name: 'visualization',
    component: visualization,
  },
  // 可以在这里添加其他路由
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;