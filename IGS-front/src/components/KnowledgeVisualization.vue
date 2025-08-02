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
            <div class="card chart-container">
                <h3>知识掌握度</h3>
                <canvas id="knowledgeChart"></canvas>
            </div>

            <!-- 学习时长图表 -->
            <div class="card chart-container">
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
    padding: 20px;
    border-bottom: 1px solid #ddd;
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

.user-info {
    display: flex;
    align-items: center;
}

.logout-btn {
    margin-left: 15px;
    padding: 5px 10px;
    background-color: #e74c3c;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.dashboard {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    width: 100%;
}

.card {
    background-color: white;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.card h3 {
    margin-bottom: 15px;
    color: #2c3e50;
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
