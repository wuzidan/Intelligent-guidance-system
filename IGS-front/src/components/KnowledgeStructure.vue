<template>
    <div class="knowledge-page">
        <header class="header">
            <h1>知识结构可视化</h1>
            <div class="user-info">
                <div class="avatar-container">
                    <div class="avatar avatar-default">
                        <span class="icon">👨‍🎓</span>
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
            <!-- 总体掌握情况卡片 -->
            <div class="card">
                <h3>总体掌握情况</h3>
                <div class="progress-item">
                    <div class="progress-label">
                        <span>知识点覆盖率</span>
                        <span>{{ coverageRate }}%</span>
                    </div>
                    <div class="progress-container">
                        <div
                            class="progress"
                            :style="{ width: coverageRate + '%' }"
                            :class="getProgressColorClass(coverageRate)"
                        ></div>
                    </div>
                </div>
                <div class="progress-item">
                    <div class="progress-label">
                        <span>已掌握知识点</span>
                        <span>{{ masteredCount }}/{{ totalCount }}</span>
                    </div>
                    <div class="progress-container">
                        <div
                            class="progress"
                            :style="{
                                width: (masteredCount / totalCount) * 100 + '%',
                            }"
                            :class="
                                getProgressColorClass(
                                    (masteredCount / totalCount) * 100
                                )
                            "
                        ></div>
                    </div>
                </div>
                <div class="progress-item">
                    <div class="progress-label">
                        <span>平均掌握程度</span>
                        <span>{{ avgMastery }}%</span>
                    </div>
                    <div class="progress-container">
                        <div
                            class="progress"
                            :style="{ width: avgMastery + '%' }"
                            :class="getProgressColorClass(avgMastery)"
                        ></div>
                    </div>
                </div>
            </div>

            <!-- 知识点分类统计卡片 -->
            <div class="card">
                <h3>知识点分类统计</h3>
                <div class="stats">
                    <div class="stat-item">
                        <span class="stat-value">{{ categoryStats.core }}</span>
                        <span class="stat-label">核心知识点</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-value">{{
                            categoryStats.important
                        }}</span>
                        <span class="stat-label">重要知识点</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-value">{{
                            categoryStats.general
                        }}</span>
                        <span class="stat-label">一般知识点</span>
                    </div>
                </div>
            </div>

            <!-- 知识点掌握度区域（增加筛选功能） -->
            <div class="content-section">
                <div class="section-header">
                    <h3>知识点掌握度</h3>
                    <!-- 筛选控件 -->
                    <div class="filter-control">
                        <label for="mastery-filter" class="filter-label"
                            >按掌握情况筛选：</label
                        >
                        <select
                            id="mastery-filter"
                            v-model="selectedLevel"
                            @change="updateMasteryChart"
                            class="mastery-select"
                        >
                            <option value="all">全部</option>
                            <option value="unmastered">未掌握（<30%）</option>
                            <option value="basic">了解（30%-50%）</option>
                            <option value="mastered">掌握（50%-70%）</option>
                            <option value="proficient">熟练（70%-90%）</option>
                            <option value="expert">精通（≥90%）</option>
                        </select>
                    </div>
                </div>
                <div class="chart-table-wrapper">
                    <div class="chart-container">
                        <canvas id="masteryChart"></canvas>
                    </div>
                    <div class="chart-table">
                        <table>
                            <thead>
                                <tr>
                                    <th>编号</th>
                                    <th>知识点</th>
                                    <th>掌握度</th>
                                    <th>等级</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr
                                    v-for="knowledge in filteredKnowledgeList"
                                    :key="knowledge.id"
                                >
                                    <td>{{ knowledge.id }}</td>
                                    <td>{{ knowledge.name }}</td>
                                    <td>{{ knowledge.mastery }}%</td>
                                    <td>
                                        <span
                                            :class="
                                                getMasteryColorClass(
                                                    knowledge.mastery,
                                                    'level'
                                                )
                                            "
                                        >
                                            {{
                                                getMasteryLevelText(
                                                    knowledge.mastery
                                                )
                                            }}
                                        </span>
                                    </td>
                                </tr>
                                <tr v-if="filteredKnowledgeList.length === 0">
                                    <td colspan="4" class="no-data">
                                        没有符合条件的知识点
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <!-- 知识点分类掌握度区域 -->
            <div class="content-section">
                <h3>知识点分类掌握度</h3>
                <div class="chart-table-wrapper">
                    <div class="chart-container">
                        <canvas id="categoryMasteryChart"></canvas>
                    </div>
                    <div class="chart-table">
                        <table>
                            <thead>
                                <tr>
                                    <th>分类</th>
                                    <th>知识点数量</th>
                                    <th>平均掌握度</th>
                                    <th>最高掌握度</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>核心知识点</td>
                                    <td>{{ categoryStats.core }}</td>
                                    <td>
                                        {{
                                            categoryAvgMastery.core.toFixed(1)
                                        }}%
                                    </td>
                                    <td>{{ categoryMaxMastery.core }}%</td>
                                </tr>
                                <tr>
                                    <td>重要知识点</td>
                                    <td>{{ categoryStats.important }}</td>
                                    <td>
                                        {{
                                            categoryAvgMastery.important.toFixed(
                                                1
                                            )
                                        }}%
                                    </td>
                                    <td>{{ categoryMaxMastery.important }}%</td>
                                </tr>
                                <tr>
                                    <td>一般知识点</td>
                                    <td>{{ categoryStats.general }}</td>
                                    <td>
                                        {{
                                            categoryAvgMastery.general.toFixed(
                                                1
                                            )
                                        }}%
                                    </td>
                                    <td>{{ categoryMaxMastery.general }}%</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <!-- 知识点详情区域 -->
            <div class="content-section">
                <h3>知识点详情</h3>
                <div class="knowledge-container">
                    <div
                        class="knowledge-card"
                        v-for="knowledge in knowledgeList"
                        :key="knowledge.id"
                        @click="showKnowledgeDetail(knowledge)"
                    >
                        <div class="knowledge-icon">
                            {{ getCategoryIcon(knowledge.category) }}
                        </div>
                        <div class="knowledge-info">
                            <h4>{{ knowledge.name }}</h4>
                            <div class="knowledge-progress-container">
                                <div
                                    class="knowledge-progress"
                                    :style="{ width: knowledge.mastery + '%' }"
                                    :class="
                                        getMasteryColorClass(knowledge.mastery)
                                    "
                                ></div>
                            </div>
                            <div class="knowledge-meta">
                                <span class="knowledge-level">{{
                                    getMasteryLevelText(knowledge.mastery)
                                }}</span>
                                <span class="knowledge-category">{{
                                    knowledge.categoryText
                                }}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- 单个知识点详情弹窗 -->
        <div class="modal" v-if="selectedKnowledge">
            <div class="modal-content">
                <span class="close" @click="selectedKnowledge = null"
                    >&times;</span
                >
                <h3>{{ selectedKnowledge.name }}</h3>
                <p class="knowledge-description">
                    {{ selectedKnowledge.description }}
                </p>

                <div class="knowledge-detail-chart">
                    <canvas id="knowledgeDetailChart"></canvas>
                </div>

                <div class="knowledge-stats">
                    <div class="stat-item">
                        <span class="stat-value"
                            >{{ selectedKnowledge.mastery }}%</span
                        >
                        <span class="stat-label">掌握程度</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-value">{{
                            selectedKnowledge.practiceCount
                        }}</span>
                        <span class="stat-label">练习次数</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-value">{{
                            selectedKnowledge.lastPracticed
                        }}</span>
                        <span class="stat-label">最后练习</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, nextTick, computed } from "vue";
import Chart from "chart.js/auto";

// 用户信息
const userName = ref("李四");
const studentId = ref("20230002");

// 总体数据
const coverageRate = ref(78);
const masteredCount = ref(25);
const totalCount = ref(60);
const avgMastery = ref(72);

// 知识点列表
const knowledgeList = ref([
    {
        id: 1,
        name: "变量与数据类型",
        category: "core",
        categoryText: "核心知识点",
        mastery: 10,
        description: "理解JavaScript中的变量声明和基本数据类型",
        practiceCount: 12,
        lastPracticed: "2023-05-15",
    },
    {
        id: 2,
        name: "函数作用域",
        category: "core",
        categoryText: "核心知识点",
        mastery: 35,
        description: "掌握函数作用域和闭包的概念",
        practiceCount: 8,
        lastPracticed: "2023-05-10",
    },
    {
        id: 3,
        name: "原型与继承",
        category: "important",
        categoryText: "重要知识点",
        mastery: 55,
        description: "理解JavaScript原型链和继承机制",
        practiceCount: 6,
        lastPracticed: "2023-05-05",
    },
    {
        id: 4,
        name: "异步编程",
        category: "important",
        categoryText: "重要知识点",
        mastery: 75,
        description: "掌握Promise和async/await的使用",
        practiceCount: 9,
        lastPracticed: "2023-05-12",
    },
    {
        id: 5,
        name: "DOM操作",
        category: "core",
        categoryText: "核心知识点",
        mastery: 85,
        description: "熟练操作DOM元素",
        practiceCount: 15,
        lastPracticed: "2023-05-14",
    },
    {
        id: 6,
        name: "事件循环",
        category: "important",
        categoryText: "重要知识点",
        mastery: 90,
        description: "理解JavaScript事件循环机制",
        practiceCount: 5,
        lastPracticed: "2023-05-08",
    },
    {
        id: 7,
        name: "模块化",
        category: "general",
        categoryText: "一般知识点",
        mastery: 95,
        description: "了解ES6模块化规范",
        practiceCount: 4,
        lastPracticed: "2023-05-03",
    },
    {
        id: 8,
        name: "设计模式",
        category: "general",
        categoryText: "一般知识点",
        mastery: 55,
        description: "了解常见的设计模式",
        practiceCount: 3,
        lastPracticed: "2023-04-28",
    },
]);

// 筛选相关变量
const selectedLevel = ref("all"); // 选中的筛选等级

// 按ID排序的知识点列表（基础数据）
const sortedKnowledgeList = computed(() => {
    return [...knowledgeList.value].sort((a, b) => a.id - b.id);
});

// 按筛选条件过滤知识点
const filteredKnowledgeList = computed(() => {
    if (selectedLevel.value === "all") {
        return sortedKnowledgeList.value;
    }
    return sortedKnowledgeList.value.filter((knowledge) => {
        const mastery = knowledge.mastery;
        switch (selectedLevel.value) {
            case "unmastered":
                return mastery < 30;
            case "basic":
                return mastery >= 30 && mastery < 50;
            case "mastered":
                return mastery >= 50 && mastery < 70;
            case "proficient":
                return mastery >= 70 && mastery < 90;
            case "expert":
                return mastery >= 90;
            default:
                return true;
        }
    });
});

// 分类统计
const categoryStats = computed(() => ({
    core: knowledgeList.value.filter((k) => k.category === "core").length,
    important: knowledgeList.value.filter((k) => k.category === "important")
        .length,
    general: knowledgeList.value.filter((k) => k.category === "general").length,
}));

// 计算分类平均掌握度
const categoryAvgMastery = computed(() => {
    const getAvg = (category) => {
        const items = knowledgeList.value.filter(
            (k) => k.category === category
        );
        return items.length
            ? items.reduce((sum, k) => sum + k.mastery, 0) / items.length
            : 0;
    };
    return {
        core: getAvg("core"),
        important: getAvg("important"),
        general: getAvg("general"),
    };
});

// 计算分类最高掌握度
const categoryMaxMastery = computed(() => {
    const getMax = (category) => {
        const items = knowledgeList.value.filter(
            (k) => k.category === category
        );
        return items.length ? Math.max(...items.map((k) => k.mastery)) : 0;
    };
    return {
        core: getMax("core"),
        important: getMax("important"),
        general: getMax("general"),
    };
});

// 选中的知识点
const selectedKnowledge = ref(null);

// 图表实例
let masteryChartInstance = null;
let categoryMasteryChartInstance = null;
let knowledgeDetailChartInstance = null;

// 根据掌握程度获取进度条颜色类
const getProgressColorClass = (progress) => {
    if (progress < 50) return "progress-low";
    if (progress < 75) return "progress-medium";
    return "progress-high";
};

// 根据掌握程度获取表格文字颜色类和进度条颜色类
const getMasteryColorClass = (mastery, type = "progress") => {
    if (type === "level") {
        if (mastery < 30) return "level-unmastered";
        if (mastery < 50) return "level-basic";
        if (mastery < 70) return "level-mastered";
        if (mastery < 90) return "level-proficient";
        return "level-expert";
    }
    return getProgressColorClass(mastery);
};

// 根据掌握程度获取文本描述
const getMasteryLevelText = (level) => {
    if (level < 30) return "未掌握";
    if (level < 50) return "了解";
    if (level < 70) return "掌握";
    if (level < 90) return "熟练";
    return "精通";
};

// 根据知识点分类获取图标
const getCategoryIcon = (category) => {
    const icons = { core: "⭐", important: "🔑", general: "📘" };
    return icons[category] || "📚";
};

// 显示知识点详情弹窗
const showKnowledgeDetail = (knowledge) => {
    selectedKnowledge.value = knowledge;
    nextTick(() => {
        renderKnowledgeDetailChart(knowledge);
    });
};

// 渲染知识点详情图表
const renderKnowledgeDetailChart = (knowledge) => {
    const ctx = document.getElementById("knowledgeDetailChart");
    if (!ctx) return;
    if (knowledgeDetailChartInstance) {
        knowledgeDetailChartInstance.destroy();
    }
    const historyData = [30, 45, 60, 55, 70, knowledge.mastery];
    const historyLabels = ["1月", "2月", "3月", "4月", "5月", "当前"];
    knowledgeDetailChartInstance = new Chart(ctx, {
        type: "line",
        data: {
            labels: historyLabels,
            datasets: [
                {
                    label: "掌握程度 (%)",
                    data: historyData,
                    borderColor: "#3498db",
                    backgroundColor: "rgba(52, 152, 219, 0.1)",
                    borderWidth: 2,
                    tension: 0.3,
                    fill: true,
                },
            ],
        },
        options: {
            responsive: true,
            scales: { y: { beginAtZero: true, max: 100 } },
        },
    });
};

// 更新知识点掌握度图表
const updateMasteryChart = () => {
    const masteryCtx = document.getElementById("masteryChart");
    if (!masteryCtx) return;

    if (masteryChartInstance) {
        masteryChartInstance.destroy();
    }

    const labels = filteredKnowledgeList.value.map((k) => `K${k.id}`);
    const data = filteredKnowledgeList.value.map((k) => k.mastery);
    const backgroundColors = filteredKnowledgeList.value.map((k) => {
        if (k.mastery < 50) return "rgba(231, 76, 60, 0.8)";
        if (k.mastery < 75) return "rgba(243, 156, 18, 0.8)";
        return "rgba(46, 204, 113, 0.8)";
    });

    masteryChartInstance = new Chart(masteryCtx, {
        type: "bar",
        data: {
            labels: labels,
            datasets: [
                {
                    label: "掌握程度 (%)",
                    data: data,
                    backgroundColor: backgroundColors,
                    borderWidth: 1,
                },
            ],
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100,
                    title: { display: true, text: "掌握度 (%)" },
                },
                x: { title: { display: true, text: "知识点编号" } },
            },
        },
    });
};

// 渲染分类掌握度图表
const renderCategoryMasteryChart = () => {
    const categoryCtx = document.getElementById("categoryMasteryChart");
    if (!categoryCtx) return;
    if (categoryMasteryChartInstance) {
        categoryMasteryChartInstance.destroy();
    }
    categoryMasteryChartInstance = new Chart(categoryCtx, {
        type: "bar",
        data: {
            labels: ["核心知识点", "重要知识点", "一般知识点"],
            datasets: [
                {
                    label: "知识点数量",
                    data: [
                        categoryStats.value.core,
                        categoryStats.value.important,
                        categoryStats.value.general,
                    ],
                    backgroundColor: [
                        "rgba(52, 152, 219, 0.7)",
                        "rgba(155, 89, 182, 0.7)",
                        "rgba(46, 204, 113, 0.7)",
                    ],
                    borderWidth: 1,
                },
            ],
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    title: { display: true, text: "知识点数量" },
                },
                x: { title: { display: true, text: "知识点分类" } },
            },
        },
    });
};

// 页面加载完成后初始化图表
onMounted(() => {
    updateMasteryChart();
    renderCategoryMasteryChart();
});

const logout = () => {
    alert("您已退出系统");
};
</script>

<style scoped>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Arial", sans-serif;
}

.knowledge-page {
    width: 100%;
    height: 100%;
    padding: 20px;
    background-color: #f4f7f9;
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
    padding: 8px 15px;
    background-color: #e74c3c;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 14px;
}

.dashboard {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    width: 100%;
}
.card,
.content-section {
    background-color: white;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    width: 100%;
    box-sizing: border-box;
}

.card h3,
.content-section h3 {
    margin: 0 0 20px 0;
    color: #2c3e50;
    font-size: 18px;
    padding-bottom: 10px;
    border-bottom: 1px solid #f0f0f0;
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

.content-section {
    grid-column: 1 / -1; /* 让内容区域横跨所有列 */
}

.chart-table-wrapper {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
}

.chart-container {
    flex: 1;
    min-width: 300px;
    position: relative;
}

.chart-table {
    flex: 1;
    min-width: 300px;
    overflow-x: auto;
}

table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
}

th,
td {
    padding: 10px 8px;
    text-align: left;
    border-bottom: 1px solid #f0f0f0;
}

th {
    background-color: #f9f9f9;
    font-weight: bold;
}

tr:hover {
    background-color: #f5f5f5;
}
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

/* 未掌握 - 纯红色 */
.level-unmastered {
    background: linear-gradient(90deg, #c0392b 0%, #e74c3c 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    font-weight: bold;
    font-size: 15px;

    font-weight: 600;
}

/* 了解 - 橙红色渐变 */
.level-basic {
    background: red;
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    font-weight: bold;
    font-size: 15px;

    font-weight: 600;
}

/* 掌握 - 蓝绿色渐变 */
.level-mastered {
    background: #f39c12;
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    font-weight: bold;
    font-size: 15px;
    font-weight: 600;
}

/* 熟练 - 浅绿色渐变 */
.level-proficient {
    background: green;
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    font-size: 15px;
    font-weight: 600;
}

/* 精通 - 深绿色渐变 */
.level-expert {
    background: linear-gradient(90deg, #1e7e34 0%, #27ae60 50%, #2ecc71 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    font-size: 15px;
    font-weight: 600;
}

.knowledge-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 20px;
    margin-top: 20px;
}

.knowledge-card {
    background-color: white;
    border-radius: 8px;
    padding: 15px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
    display: flex;
    align-items: center;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
    border: 1px solid #eee;
}

.knowledge-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.knowledge-icon {
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

.knowledge-info {
    flex: 1;
}

.knowledge-info h4 {
    margin-bottom: 8px;
    color: #2c3e50;
    font-size: 16px;
}

.knowledge-progress-container {
    width: 100%;
    height: 8px;
    background-color: #f0f0f0;
    border-radius: 4px;
    overflow: hidden;
    margin-bottom: 5px;
}

.knowledge-progress {
    height: 100%;
    transition: width 0.3s ease;
}

.knowledge-meta {
    display: flex;
    justify-content: space-between;
    font-size: 12px;
}

.knowledge-level {
    font-weight: bold;
}

.knowledge-category {
    color: #7f8c8d;
}

.modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

.modal-content {
    background-color: white;
    padding: 25px;
    border-radius: 8px;
    width: 90%;
    max-width: 700px;
    max-height: 90vh;
    overflow-y: auto;
    position: relative;
}

.close {
    position: absolute;
    top: 15px;
    right: 15px;
    font-size: 24px;
    cursor: pointer;
    color: #7f8c8d;
}

.knowledge-description {
    margin: 15px 0;
    color: #34495e;
    line-height: 1.6;
}

.knowledge-detail-chart {
    height: 250px;
    margin: 20px 0;
}

.knowledge-stats {
    display: flex;
    justify-content: space-around;
    margin-top: 20px;
}

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

.section-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 15px;
}

.filter-control {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 8px 15px;
    background-color: #f8fafc;
    border-radius: 8px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

.filter-control label {
    font-weight: 500;
    color: #334155;
    font-size: 0.95em;
    white-space: nowrap;
}

.filter-control select {
    padding: 8px 30px 8px 14px;
    border-radius: 6px;
    border: 1px solid #e2e8f0;
    background-color: #fff;
    font-size: 0.9em;
    color: #1e293b;
    appearance: none;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%2364748b' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: right 12px center;
    cursor: pointer;
    transition: all 0.2s ease;
}

.filter-control select:hover {
    border-color: #94a3b8;
}

.filter-control select:focus {
    outline: none;
    border-color: #3b82f6;
    box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.1);
}

/* 选项样式优化 */
.filter-control select option {
    padding: 8px;
    background-color: #fff;
    color: #1e293b;
}

.filter-control select option:hover {
    background-color: #f1f5f9;
}

.no-data {
    text-align: center;
    color: #888;
    padding: 20px;
    font-style: italic;
}

@media (max-width: 768px) {
    .dashboard {
        grid-template-columns: 1fr;
    }

    .chart-table-wrapper {
        flex-direction: column;
    }

    .section-header {
        flex-direction: column;
        align-items: flex-start;
        gap: 10px;
    }
}
</style>
