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
          <li><a href="#" :class="{ 'active-submenu': activeSubmenu === '题库' }" @click="setActiveSubmenu('题库')">题库</a></li>
          <li><a href="#" :class="{ 'active-submenu': activeSubmenu === '作答历史' }" @click="setActiveSubmenu('作答历史')">作答历史</a></li>
        </ul>
      </li>
      <li class="menu-item" :class="{ active: activeMenu === 'knowledge' }">
        <div class="menu-title" @click="toggleMenu('knowledge')">
          <span class="icon">📊</span>
          <span>知识状态</span>
        </div>
        <ul class="submenu" v-if="activeMenu === 'knowledge'">
          <li><router-link to="/" :class="{ 'active-submenu': activeSubmenu === '知识可视化' }" @click="setActiveSubmenu('状态可视化')">状态可视化</router-link></li>
          <li><a href="#" :class="{ 'active-submenu': activeSubmenu === '知识结构' }" @click="setActiveSubmenu('知识结构')">知识结构</a></li>
        </ul>
      </li>
      <li class="menu-item" :class="{ active: activeMenu === 'info' }">
        <div class="menu-title" @click="toggleMenu('info')">
          <span class="icon">👤</span>
          <span>信息模块</span>
        </div>
        <ul class="submenu" v-if="activeMenu === 'info'">
          <li><router-link to="/user-info" :class="{ 'active-submenu': activeSubmenu === '个人信息' }" @click="setActiveSubmenu('个人信息')">个人信息</router-link></li>
        </ul>
      </li>
    </ul>
  </nav>
</template>

<script>
// 侧边栏组件脚本
import { ref } from 'vue';
import { RouterLink } from 'vue-router';

export default {
  name: 'AppSidebar',
  setup() {
    // 响应式引用，用于跟踪当前激活的菜单
    const activeMenu = ref('knowledge');
    // 响应式引用，用于跟踪当前激活的子菜单
    const activeSubmenu = ref('状态可视化');
    
    // 切换菜单展开/收起状态的函数
    const toggleMenu = (menuName) => {
      activeMenu.value = activeMenu.value === menuName ? '' : menuName;
    };
    
    // 设置当前激活的子菜单
    const setActiveSubmenu = (submenuName) => {
      activeSubmenu.value = submenuName;
    };
    
    // 暴露状态和方法给模板使用
    return {
      activeMenu,
      activeSubmenu,
      toggleMenu,
      setActiveSubmenu
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

/* 激活的子菜单样式 */
.submenu li a.active-submenu {
  background-color: #34495e;
  color: white;
  font-weight: bold;
}
</style>