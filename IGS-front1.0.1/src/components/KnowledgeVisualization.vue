<template>
    <div class="visualization-page">
        <header class="header">
            <h1>状态可视化</h1>
            <div class="user-info">
                <div class="avatar-container">
                    <div class="avatar avatar-default">
                        <span class="icon">{{ userAvatar }}</span>
                    </div>
                    <div class="user-basic">
                        <h2>{{ userName }}</h2>
                        <p class="user-id">{{ studentId }}</p>
                    </div>
                </div>
                <button class="logout-btn" @click="logout">退出</button>
            </div>
        </header>

        <div class="dashboard">
            <!-- 学习进度卡片 -->
            <div class="card">
                <h3>学习进度</h3>
                <div class="progress-item">
                    <div class="progress-label">
                        <span>总体进度</span>
                        <span>{{ overallProgress }}%</span>
                    </div>
                    <div class="progress-container">
                        <div
                            class="progress"
                            :style="{ width: overallProgress + '%' }"
                            :class="getProgressColorClass(overallProgress)"
                        ></div>
                    </div>
                </div>
                <div class="progress-item">
                    <div class="progress-label">
                        <span>已完成课程</span>
                        <span>{{ completedCourses }}/{{ totalCourses }}</span>
                    </div>
                    <div class="progress-container">
                        <div
                            class="progress"
                            :style="{
                                width:
                                    (completedCourses / totalCourses) * 100 +
                                    '%',
                            }"
                            :class="
                                getProgressColorClass(
                                    (completedCourses / totalCourses) * 100
                                )
                            "
                        ></div>
                    </div>
                </div>
                <div class="progress-item">
                    <div class="progress-label">
                        <span>平均成绩</span>
                        <span>{{ avgScore }}分</span>
                    </div>
                    <div class="progress-container">
                        <div
                            class="progress"
                            :style="{ width: avgScore + '%' }"
                            :class="getProgressColorClass(avgScore)"
                        ></div>
                    </div>
                </div>
            </div>

            <!-- 答题统计卡片 -->
            <div class="card">
                <h3>答题统计</h3>
                <div class="stats">
                    <div class="stat-item">
                        <span class="stat-value">85</span>
                        <span class="stat-label">正确率</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-value">120</span>
                        <span class="stat-label">总题数</span>
                    </div>
                </div>
            </div>

            <!-- 知识掌握度图表 -->
            <div class="chart-container">
                <h3>知识掌握度</h3>
                <canvas id="knowledgeChart"></canvas>
            </div>

            <!-- 学习时长图表 -->
            <div class="chart-container">
                <h3>学习时长</h3>
                <canvas id="learningHoursChart"></canvas>
            </div>
        </div>

        <!-- 编程技能部分 -->
        <div class="skill-section">
            <h3>编程技能</h3>
            <div class="skills-container">
                <div
                    class="skill-card"
                    v-for="skill in skills"
                    :key="skill.name"
                >
                    <div class="skill-icon">{{ skill.icon }}</div>
                    <div class="skill-info">
                        <h4>{{ skill.name }}</h4>
                        <div class="skill-progress-container">
                            <div
                                class="skill-progress"
                                :style="{ width: skill.level + '%' }"
                                :class="getSkillColorClass(skill.level)"
                            ></div>
                        </div>
                        <p class="skill-level">
                            {{ getSkillLevelText(skill.level) }}
                        </p>
                    </div>
                </div>
            </div>
        </div>

        <!-- 最近活动 -->
        <!-- <div class="card activity">
        <h3>最近活动</h3>
        <ul class="activity-list">
          <li>完成了"HTML基础"章节测试</li>
          <li>学习了"CSS布局"课程</li>
          <li>提交了"JavaScript基础"作业</li>
        </ul>
      </div> -->
    </div>
</template>

<script>
// 知识状态可视化组件脚本
import { onMounted, ref } from "vue";
import Chart from "chart.js/auto";

// 注意：AppSidebar 组件在模板中未使用，已移除导入

export default {
    name: "KnowledgeVisualization",
    setup() {
        // 退出功能
        const logout = () => {
            alert("您已退出系统");
        };

        // 学习进度数据
        const overallProgress = ref(65);
        const completedCourses = ref(8);
        const totalCourses = ref(12);
        const avgScore = ref(85);
        const userName = ref("张三");
        const studentId = ref("20230001");
        const userAvatar = ref("👨‍💻");

        // 编程技能数据
        const skills = ref([
            { name: "JavaScript", icon: "⚡", level: 75 },
            { name: "Python", icon: "🐍", level: 65 },
            { name: "Java", icon: "☕", level: 50 },
            { name: "HTML/CSS", icon: "🌐", level: 85 },
            { name: "Git", icon: "🔀", level: 60 },
            { name: "SQL", icon: "🗃️", level: 55 },
        ]);

        // 根据进度获取颜色类
        const getProgressColorClass = (progress) => {
            if (progress < 50) return "progress-low";
            if (progress < 75) return "progress-medium";
            return "progress-high";
        };

        // 根据技能水平获取颜色类
        const getSkillColorClass = (level) => {
            if (level < 40) return "skill-low";
            if (level < 70) return "skill-medium";
            return "skill-high";
        };

        // 获取技能水平文本描述
        const getSkillLevelText = (level) => {
            if (level < 20) return "入门";
            if (level < 40) return "基础";
            if (level < 60) return "中级";
            if (level < 80) return "高级";
            return "专家";
        };

        // 页面加载完成后初始化图表
        onMounted(() => {
            // 初始化知识掌握度雷达图
            const knowledgeCtx = document
                .getElementById("knowledgeChart")
                .getContext("2d");
            new Chart(knowledgeCtx, {
                type: "radar",
                data: {
                    labels: [
                        "HTML",
                        "CSS",
                        "JavaScript",
                        "数据库",
                        "算法",
                        "网络",
                    ],
                    datasets: [
                        {
                            label: "掌握程度",
                            data: [85, 75, 65, 60, 50, 70],
                            backgroundColor: "rgba(52, 152, 219, 0.2)",
                            borderColor: "rgba(52, 152, 219, 1)",
                            borderWidth: 2,
                            pointBackgroundColor: "rgba(52, 152, 219, 1)",
                        },
                    ],
                },
                options: {
                    scales: {
                        r: {
                            angleLines: { display: true },
                            suggestedMin: 0,
                            suggestedMax: 100,
                        },
                    },
                },
            });

            // 初始化学习进度柱状图
            const progressCtx = document
                .getElementById("learningHoursChart")
                .getContext("2d");
            new Chart(progressCtx, {
                type: "bar",
                data: {
                    labels: ["1月", "2月", "3月", "4月", "5月"],
                    datasets: [
                        {
                            label: "学习时长(小时)",
                            data: [30, 45, 60, 50, 40],
                            backgroundColor: "rgba(46, 204, 113, 0.6)",
                            borderColor: "rgba(46, 204, 113, 1)",
                            borderWidth: 1,
                        },
                    ],
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true,
                        },
                    },
                },
            });
        });

        return {
            logout,
            overallProgress,
            completedCourses,
            totalCourses,
            avgScore,
            userName,
            studentId,
            userAvatar,
            skills,
            getProgressColorClass,
            getSkillColorClass,
            getSkillLevelText,
        };
    },
};
</script>

<style scoped>
/* 页面样式 */
.visualization-page {
    width: 100%;
    height: 100%;
    padding: 20px;
}

/* 全局样式 */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Arial", sans-serif;
}

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    padding: 18px 24px; /* 调整内边距，上下稍窄左右稍宽 */
    border-bottom: 2px solid transparent;
    border-image: linear-gradient(90deg, #3498db, #9b59b6) 1; /* 渐变色下边框 */
    background: linear-gradient(
        135deg,
        #ffffff 0%,
        #f8fafc 100%
    ); /* 微妙的渐变背景 */
    border-radius: 12px; /* 增大圆角，更柔和 */
    box-shadow: 0 4px 20px rgba(52, 152, 219, 0.08); /* 浅蓝色调阴影，与主题呼应 */
    position: relative;
    overflow: hidden;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); /* 统一动画曲线 */
}

/* 顶部高光装饰 */
.header::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: linear-gradient(90deg, #3498db, #9b59b6, #3498db);
    background-size: 200% 100%;
    animation: headerGlow 6s ease-in-out infinite; /* 渐变光流动画 */
}

/* 标题文字样式优化 */
.header h1 {
    margin: 0;
    font-size: 30px;
    font-weight: 600;
    background: linear-gradient(90deg, #2c3e50, #34495e);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    position: relative;
    padding-left: 12px;
    transition: transform 0.3s ease;
}

/* 标题左侧小装饰 */
.header h1::before {
    content: "";
    position: absolute;
    left: 0;
    top: 50%;
    transform: translateY(-50%);
    width: 4px;
    height: 60%;
    border-radius: 2px;
    background: linear-gradient(180deg, #3498db, #9b59b6);
}

/* 用户信息区域动画 */
.user-info {
    display: flex;
    align-items: center;
    transition: transform 0.3s ease;
}

/* 退出按钮美化 */
.logout-btn {
    margin-left: 15px;
    padding: 9px 18px;
    background: linear-gradient(90deg, #3498db, #2980b9);
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 14px;
    font-weight: 500;
    box-shadow: 0 2px 8px rgba(52, 152, 219, 0.3);
    transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    position: relative;
    overflow: hidden;
}

/* 按钮悬停效果 */
.logout-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(52, 152, 219, 0.4);
    background: linear-gradient(90deg, #2980b9, #3498db);
}

/* 按钮点击波纹效果 */
.logout-btn::after {
    content: "";
    position: absolute;
    top: 50%;
    left: 50%;
    width: 120px;
    height: 120px;
    background: rgba(255, 255, 255, 0.2);
    border-radius: 50%;
    transform: translate(-50%, -50%) scale(0);
    transition: transform 0.6s ease;
}

.logout-btn:active::after {
    transform: translate(-50%, -50%) scale(1);
}

/* 整体悬停动画 */
.header:hover {
    box-shadow: 0 6px 25px rgba(52, 152, 219, 0.12);
    transform: translateY(-2px);
}

.header:hover h1 {
    transform: translateX(5px);
}

.header:hover .user-info {
    transform: translateX(-5px);
}

/* 顶部渐变光流动画 */
@keyframes headerGlow {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}

.user-info {
    font-size: 15px;
    display: flex;
    align-items: center;
}

.logout-btn {
    margin-left: 15px;
    padding: 8px 15px;
    background-color: #e74c3c;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
}

.dashboard {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    width: 100%;
}

.card {
    background: linear-gradient(145deg, #ffffff 0%, #f0f7ff 100%);
    border-radius: 10px;
    padding: 22px;
    box-shadow: 0 3px 12px rgba(59, 130, 246, 0.08);
    border: 1px solid rgba(240, 249, 255, 0.8);
    position: relative;
    overflow: hidden;
    transition: all 0.4s cubic-bezier(0.22, 1, 0.36, 1);
}

/* 左侧蓝色渐变装饰条 */
.card::before {
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    height: 100%;
    width: 4px;
    background: linear-gradient(180deg, #60a5fa 0%, #2563eb 100%);
    transform: scaleY(0.8);
    opacity: 0.7;
    transition: all 0.4s ease;
}

/* 顶部横向渐变光条 */
.card::after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 3px;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(59, 130, 246, 0.25),
        transparent
    );
    transform: translateX(-100%);
    transition: transform 0.7s ease-in-out;
}

.card h3 {
    margin-bottom: 18px;
    color: #1e3a8a;
    font-size: 18px;
    font-weight: 600;
    padding-bottom: 8px;
    border-bottom: 1px dashed rgba(59, 130, 246, 0.2);
    position: relative;
    display: inline-block;
    transition: color 0.3s ease;
}

/* 标题前蓝色装饰图标 */
.card h3::before {
    content: "▷";
    display: inline-block;
    margin-right: 8px;
    font-size: 14px;
    color: #3b82f6;
    vertical-align: middle;
    transform: scale(0.9) translateX(-2px);
    transition: transform 0.3s ease;
}

/* 悬停动画效果 */
.card:hover {
    transform: translateY(-5px) scale(1.01);
    box-shadow: 0 10px 25px rgba(59, 130, 246, 0.15);
    border-color: rgba(191, 219, 254, 0.8);
}

.card:hover::before {
    transform: scaleY(1);
    opacity: 1;
}

.card:hover::after {
    transform: translateX(100%);
}

.card:hover h3 {
    color: #2563eb;
}

.card:hover h3::before {
    transform: scale(1.2) translateX(0) rotate(90deg);
    color: #2563eb;
}

/* 卡片内元素延迟动画 */
.card .progress-item,
.card .stat-item {
    transition: transform 0.3s ease, opacity 0.3s ease;
    opacity: 0.9;
}

.card:hover .progress-item,
.card:hover .stat-item {
    transform: translateX(3px);
    opacity: 1;
}

/* 子元素依次动画 */
.card:hover .progress-item:nth-child(2),
.card:hover .stat-item:nth-child(2) {
    transition-delay: 0.1s;
}

.card:hover .progress-item:nth-child(3),
.card:hover .stat-item:nth-child(3) {
    transition-delay: 0.2s;
}

.stats {
    display: flex;
    justify-content: space-around;
}

.stat-item {
    text-align: center;
}

.stat-value {
    display: block;
    font-size: 24px;
    font-weight: bold;
    color: #3498db;
}

.stat-label {
    color: #7f8c8d;
    font-size: 14px;
}

.chart-container {
    height: 300px;
}

.activity-list {
    list-style: none;
}

.activity-list li {
    padding: 8px 0;
    border-bottom: 1px solid #eee;
}

.activity-list li:last-child {
    border-bottom: none;
}

.activity {
    margin-top: 20px;
}

/* 进度条样式 */
.progress-item {
    margin-bottom: 15px;
}

.progress-label {
    display: flex;
    justify-content: space-between;
    margin-bottom: 5px;
    font-size: 14px;
}

.progress-container {
    width: 100%;
    height: 10px;
    background-color: #f0f0f0;
    border-radius: 5px; /* 容器保持圆角 */
    overflow: hidden;
}

.progress {
    height: 100%;
    transition: width 0.3s ease;
    border-radius: 5px; /* 为进度条添加圆角 */
}

/* 红色渐变 - 低进度 */
.progress-low {
    background: linear-gradient(90deg, #c0392b 0%, #e74c3c 100%);
}

/* 黄色渐变 - 中等进度 */
.progress-medium {
    background: linear-gradient(90deg, #d35400 0%, #f39c12 50%, #f1c40f 100%);
}

/* 绿色渐变 - 高进度 */
.progress-high {
    background: linear-gradient(90deg, #1e7e34 0%, #2ecc71 50%, #81c784 100%);
}

/* 技能卡片样式 */
.skill-section {
    margin-top: 30px;
}

.skills-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 20px;
    margin-top: 20px;
}

.skill-card {
    background-color: white;
    border-radius: 8px;
    padding: 15px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    display: flex;
    align-items: center;
}

.skill-icon {
    font-size: 24px;
    margin-right: 15px;
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #f0f2f5;
    border-radius: 50%;
}

.skill-info {
    flex: 1;
}

.skill-info h4 {
    margin-bottom: 8px;
    color: #2c3e50;
}

.skill-progress-container {
    width: 100%;
    height: 8px;
    background-color: #f0f0f0;
    border-radius: 4px;
    overflow: hidden;
    margin-bottom: 5px;
}

.skill-progress {
    height: 100%;
    transition: width 0.3s ease;
}

.skill-low {
    background-color: #e74c3c;
}

.skill-medium {
    background-color: #f39c12;
}

.skill-high {
    background-color: #2ecc71;
}

.skill-level {
    font-size: 12px;
    color: #7f8c8d;
}

/* 用户信息样式 */
.avatar-container {
    display: flex;
    align-items: center;
}

.avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    margin-right: 10px;
}

.avatar-default {
    background-color: #3498db;
    color: white;
}

.user-basic {
    margin: 0;
}

.user-basic h2 {
    font-size: 16px;
    margin: 0;
    color: #2c3e50;
}

.user-id {
    font-size: 12px;
    color: #7f8c8d;
    margin: 0;
}
</style>
