<template>
  <!-- 左侧导航栏 -->
  <nav class="sidebar">
    <div class="logo">智能导学系统</div>
    <ul class="menu">
      <li class="menu-item" :class="{ active: activeMenu === 'answer' }">
        <div class="menu-title" @click="toggleMenu('answer')">
          <span class="icon">📝</span>
          <span>答题模块</span>
        </div>
        <ul class="submenu" v-if="activeMenu === 'answer'">
          <li><a href="#">题库</a></li>
          <li><a href="#">作答历史</a></li>
        </ul>
      </li>
      <li class="menu-item" :class="{ active: activeMenu === 'knowledge' }">
        <div class="menu-title" @click="toggleMenu('knowledge')">
          <span class="icon">📊</span>
          <span>知识状态</span>
        </div>
        <ul class="submenu" v-if="activeMenu === 'knowledge'">
          <li><a href="#">状态可视化</a></li>
          <li><a href="#">知识结构</a></li>
        </ul>
      </li>
      <li class="menu-item" :class="{ active: activeMenu === 'info' }">
        <div class="menu-title" @click="toggleMenu('info')">
          <span class="icon">👤</span>
          <span>信息模块</span>
        </div>
        <ul class="submenu" v-if="activeMenu === 'info'">
          <li><a href="#">个人信息</a></li>
        </ul>
      </li>
    </ul>
  </nav>
</template>

<script>
// 侧边栏组件脚本
import { ref } from 'vue';

export default {
  name: 'AppSidebar',
  setup() {
    // 响应式引用，用于跟踪当前激活的菜单
    const activeMenu = ref('knowledge');
    
    // 切换菜单展开/收起状态的函数
    const toggleMenu = (menuName) => {
      activeMenu.value = activeMenu.value === menuName ? '' : menuName;
    };
    
    // 暴露状态和方法给模板使用
    return {
      activeMenu,
      toggleMenu
    };
  }
};
</script>

<style scoped>
/* 侧边栏样式 */
.sidebar {
  width: 250px;
  background-color: #2c3e50;
  color: white;
  padding: 20px 0;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 100;
}

.logo {
  font-size: 20px;
  font-weight: bold;
  padding: 0 20px 20px;
  border-bottom: 1px solid #34495e;
  margin-bottom: 20px;
}

.menu {
  list-style: none;
}

.menu-item {
  margin-bottom: 5px;
}

.menu-title {
  padding: 12px 20px;
  display: flex;
  align-items: center;
  cursor: pointer;
  transition: background-color 0.3s;
}

.menu-title:hover {
  background-color: #34495e;
}

.menu-title .icon {
  margin-right: 10px;
  font-size: 18px;
}

.submenu {
  list-style: none;
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease-out;
}

.menu-item.active .submenu {
  max-height: 200px;
}

.submenu li a {
  display: block;
  padding: 10px 20px 10px 50px;
  color: #bdc3c7;
  text-decoration: none;
  transition: background-color 0.3s, color 0.3s;
}

.submenu li a:hover {
  background-color: #34495e;
  color: white;
}
</style>