import { createRouter, createWebHistory } from 'vue-router';
import visualization from '../components/KnowledgeVisualization.vue';
import userInfo from '../components/UserInfo.vue';
import knowledgeStructure from '../components/knowledgeStructure.vue';
import quizChallenge from '../components/quizChallenge.vue';
import history from '../components/history.vue';

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
  {
    path: '/knowledge-structure',
    name: 'knowledge-structure',
    component: knowledgeStructure,
  },
  {
    path: '/quiz-challenge',
    name: 'quiz-challenge',
    component: quizChallenge,
  },
  {
    path: '/history',
    name: 'history',
    component: history,
  },
  // 可以在这里添加其他路由
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;