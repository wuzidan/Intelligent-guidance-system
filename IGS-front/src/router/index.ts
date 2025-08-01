import { createRouter, createWebHistory } from 'vue-router';
import visualization from '../components/KnowledgeVisualization.vue';
import userInfo from '../components/UserInfo.vue';

const routes = [
  {
    path: '/',
    name: 'visualization',
    component: visualization,
  },
  {
    path: '/user-info',
    name: 'userInfo',
    component: userInfo,
  },
  // 可以在这里添加其他路由
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;