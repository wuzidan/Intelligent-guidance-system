<template>
  <div class="visualization-page">
    <header class="header">
      <h1>知识状态可视化</h1>
      <div class="user-info">
        <span>欢迎，张三</span>
        <button class="logout-btn" @click="logout">退出</button>
      </div>
    </header>

    <div class="dashboard">
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

        <!-- 学习进度图表 -->
        <div class="card chart-container">
          <h3>学习进度</h3>
          <canvas id="progressChart"></canvas>
        </div>

        <!-- 最近活动 -->
        <div class="card activity">
          <h3>最近活动</h3>
          <ul class="activity-list">
            <li>完成了"HTML基础"章节测试</li>
            <li>学习了"CSS布局"课程</li>
            <li>提交了"JavaScript基础"作业</li>
          </ul>
        </div>
      </div>
  </div>
</template>

<script>
// 知识状态可视化组件脚本
import { onMounted } from 'vue';
import Chart from 'chart.js/auto';

// 注意：AppSidebar 组件在模板中未使用，已移除导入

export default {
  name: 'VisualizationOfState',
  setup() {
    // 退出功能
    const logout = () => {
      alert('您已退出系统');
    };

    // 页面加载完成后初始化图表
    onMounted(() => {
      // 初始化知识掌握度雷达图
      const knowledgeCtx = document.getElementById('knowledgeChart').getContext('2d');
      new Chart(knowledgeCtx, {
        type: 'radar',
        data: {
          labels: ['HTML', 'CSS', 'JavaScript', '数据库', '算法', '网络'],
          datasets: [{
            label: '掌握程度',
            data: [85, 75, 65, 60, 50, 70],
            backgroundColor: 'rgba(52, 152, 219, 0.2)',
            borderColor: 'rgba(52, 152, 219, 1)',
            borderWidth: 2,
            pointBackgroundColor: 'rgba(52, 152, 219, 1)'
          }]
        },
        options: {
          scales: {
            r: {
              angleLines: { display: true },
              suggestedMin: 0,
              suggestedMax: 100
            }
          }
        }
      });

      // 初始化学习进度柱状图
      const progressCtx = document.getElementById('progressChart').getContext('2d');
      new Chart(progressCtx, {
        type: 'bar',
        data: {
          labels: ['1月', '2月', '3月', '4月', '5月'],
          datasets: [{
            label: '学习时长(小时)',
            data: [30, 45, 60, 50, 40],
            backgroundColor: 'rgba(46, 204, 113, 0.6)',
            borderColor: 'rgba(46, 204, 113, 1)',
            borderWidth: 1
          }]
        },
        options: {
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
    });

    return {
      logout
    };
  }
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
  font-family: 'Arial', sans-serif;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  padding-bottom: 20px;
  border-bottom: 1px solid #ddd;
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
</style>