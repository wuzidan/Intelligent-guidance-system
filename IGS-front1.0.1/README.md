# 智能导学系统 - 前端项目

## 项目简介
智能导学系统是一个面向计算机编程技能学习的智能辅导平台，旨在帮助学生更好地掌握编程知识和技能。本项目为系统的前端部分，采用现代Web技术栈开发，提供友好的用户界面和丰富的学习功能。

## 技术栈
- **框架**: Vue 3 (Composition API)
- **路由**: Vue Router
- **构建工具**: Vite
- **语言**: JavaScript
- **样式**: CSS (Scoped Style)

## 项目结构
```
IGS-front/
├── .gitignore
├── .vscode/
├── README.md
├── env.d.ts
├── index.html
├── package-lock.json
├── package.json
├── public/
├── src/
│   ├── App.vue
│   ├── components/
│   │   ├── AppSidebar.vue     # 侧边栏组件
│   │   ├── UserInfo.vue       # 个人信息组件
│   │   ├── icons/             # 图标组件
│   │   └── visualization-of-state.vue  # 知识状态可视化组件
│   ├── main.ts
│   ├── router/
│   │   └── index.ts           # 路由配置
│   └── shims-vue.d.ts
├── tsconfig.app.json
├── tsconfig.json
├── tsconfig.node.json
└── vite.config.ts
```

## 功能模块
1. **答题模块**
   - 题库管理
   - 作答历史记录

2. **知识状态**
   - 状态可视化展示
   - 知识结构分析

3. **信息模块**
   - 个人信息管理

## 协作指南
1. **代码规范**
   - 使用JavaScript编写组件逻辑
   - 遵循Vue 3 Composition API风格
   - 组件样式使用scoped属性隔离
   - 提交代码前确保代码格式化

## 注意事项
1. 请不要将敏感信息提交到代码仓库
2. 保持代码简洁、可维护
3. 新功能开发前请先讨论方案
4. 遇到问题及时沟通，避免长时间卡壳
5. 定期更新本地代码，避免冲突

## 项目设置

```sh
npm install
```

### 开发环境运行（带热更新）

```sh
npm run dev
```

### 类型检查、编译和生产环境构建

```sh
npm run build
```
