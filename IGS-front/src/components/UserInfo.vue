<template>
  <div class="user-info-container">
    <div class="user-info-header">
      <div class="header-content">
        <div class="avatar-container">
          <div class="avatar" :class="avatarClass">
            <span class="icon">{{ userAvatar }}</span>
          </div>
          <div class="user-basic">
            <h2>{{ userName }}</h2>
            <p class="user-id">{{ studentId }}</p>
            <p class="user-class">{{ className }}</p>
            <p class="user-major">{{ major }}</p>
          </div>
        </div>
        <button class="edit-btn" @click="toggleEditMode">
          <span v-if="!isEditing">编辑信息</span>
          <span v-if="isEditing">保存</span>
        </button>
      </div>
    </div>
    
    <div class="user-info-content">
      <div class="info-card" :class="{ 'editing': isEditing }">
        <h3>基本信息</h3>
        <div class="info-item">
          <label>出生日期:</label>
          <template v-if="isEditing">
            <input type="date" v-model="birthDate">
          </template>
          <span v-else>{{ birthDate }}</span>
        </div>
        <div class="info-item">
          <label>籍贯:</label>
          <template v-if="isEditing">
            <input type="text" v-model="hometown" placeholder="输入籍贯">
          </template>
          <span v-else>{{ hometown }}</span>
        </div>
        <div class="info-item">
          <label>政治面貌:</label>
          <template v-if="isEditing">
            <select v-model="politicalStatus">
              <option value="群众">群众</option>
              <option value="团员">团员</option>
              <option value="党员">党员</option>
              <option value="预备党员">预备党员</option>
            </select>
          </template>
          <span v-else>{{ politicalStatus }}</span>
        </div>
      </div>

      <div class="info-card" :class="{ 'editing': isEditing }">
        <h3>联系方式</h3>
        <div class="info-item">
          <label>电子邮箱:</label>
          <template v-if="isEditing">
            <input type="email" v-model="email" placeholder="输入电子邮箱">
          </template>
          <span v-else>{{ email }}</span>
        </div>
        <div class="info-item">
          <label>联系电话:</label>
          <template v-if="isEditing">
            <input type="tel" v-model="phone" placeholder="输入联系电话">
          </template>
          <span v-else>{{ phone }}</span>
        </div>
        <div class="info-item">
          <label>个人网站:</label>
          <template v-if="isEditing">
            <input type="url" v-model="website" placeholder="输入个人网站">
          </template>
          <span v-else>{{ website || '未设置' }}</span>
        </div>
      </div>

      <div class="info-card" :class="{ 'editing': isEditing }">
        <h3>个人简介</h3>
        <div class="info-item full-width">
          <template v-if="isEditing">
            <textarea v-model="bio" placeholder="输入个人简介" rows="5"></textarea>
          </template>
          <span v-else>{{ bio }}</span>
        </div>
      </div>

      <div class="info-card" :class="{ 'editing': isEditing }">
        <h3>兴趣爱好</h3>
        <div class="hobbies-container">
          <template v-if="isEditing">
            <div class="hobby-input">
              <input type="text" v-model="newHobby" placeholder="添加兴趣爱好">
              <button @click="addHobby">添加</button>
            </div>
          </template>
          <div class="hobby-tags">
            <span v-for="(hobby, index) in hobbies" :key="index" class="hobby-tag">
              {{ hobby }}
              <span v-if="isEditing" class="remove-hobby" @click.stop="removeHobby(index)">×</span>
            </span>
          </div>
        </div>
      </div>

      <div class="info-card" :class="{ 'editing': isEditing }">
        <h3>技能特长</h3>
        <div class="skills-container">
          <div v-for="(skill, index) in skills" :key="index" class="skill-item">
            <div class="skill-name">
              <template v-if="isEditing">
                <input type="text" v-model="skill.name" placeholder="技能名称">
              </template>
              <span v-else>{{ skill.name }}</span>
            </div>
            <div class="skill-level">
              <template v-if="isEditing">
                <select v-model="skill.level">
                  <option value="初级">初级</option>
                  <option value="中级">中级</option>
                  <option value="高级">高级</option>
                  <option value="精通">精通</option>
                </select>
              </template>
              <span v-else>{{ skill.level }}</span>
            </div>
            <div v-if="isEditing" class="skill-actions">
              <button @click="removeSkill(index)">删除</button>
            </div>
          </div>
          <div v-if="isEditing" class="add-skill">
            <button @click="addSkill">添加技能</button>
          </div>
        </div>
      </div>

      <div class="info-card" :class="{ 'editing': isEditing }">
        <h3>教育经历</h3>
        <div class="education-container">
          <div v-for="(edu, index) in education" :key="index" class="education-item">
            <div class="edu-school">
              <template v-if="isEditing">
                <input type="text" v-model="edu.school" placeholder="学校名称">
              </template>
              <span v-else>{{ edu.school }}</span>
            </div>
            <div class="edu-period">
              <template v-if="isEditing">
                <input type="text" v-model="edu.period" placeholder="时间段 (如: 2020.09-2024.06)">
              </template>
              <span v-else>{{ edu.period }}</span>
            </div>
            <div class="edu-major">
              <template v-if="isEditing">
                <input type="text" v-model="edu.major" placeholder="专业">
              </template>
              <span v-else>{{ edu.major }}</span>
            </div>
            <div class="edu-degree">
              <template v-if="isEditing">
                <select v-model="edu.degree">
                  <option value="本科">本科</option>
                  <option value="硕士">硕士</option>
                  <option value="博士">博士</option>
                </select>
              </template>
              <span v-else>{{ edu.degree }}</span>
            </div>
            <div v-if="isEditing" class="edu-actions">
              <button @click="removeEducation(index)">删除</button>
            </div>
          </div>
          <div v-if="isEditing" class="add-education">
            <button @click="addEducation">添加教育经历</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue';

export default {
  name: 'UserInfo',
  setup() {
    // 响应式数据
    const isEditing = ref(false);
    const userName = ref('张三');
    const studentId = ref('20230001');
    const className = ref('计算机科学与技术 2023级');
    const major = ref('计算机科学与技术');
    const birthDate = ref('2005-01-15');
    const hometown = ref('广东省广州市');
    const politicalStatus = ref('团员');
    const email = ref('zhangsan@example.com');
    const phone = ref('13800138000');
    const website = ref('');
    const bio = ref('我是一名计算机科学与技术专业的学生，热爱编程和学习新技术。我对人工智能和大数据分析特别感兴趣，希望未来能在这些领域发展。');
    const userAvatar = ref('👨‍💻');
    const hobbies = ref(['编程', '篮球', '音乐', '阅读']);
    const newHobby = ref('');
    const skills = ref([
      { name: 'JavaScript', level: '中级' },
      { name: 'Python', level: '初级' },
      { name: 'HTML/CSS', level: '高级' },
      { name: 'Vue.js', level: '中级' }
    ]);
    const education = ref([
      { school: '华南师范大学', period: '2023.09-至今', major: '计算机科学与技术', degree: '本科' }
    ]);

    // 切换编辑模式
    const toggleEditMode = () => {
      isEditing.value = !isEditing.value;
      // 如果退出编辑模式，可以在这里添加保存逻辑
      if (!isEditing.value) {
        // 这里可以添加保存逻辑，例如调用API保存数据
        console.log('保存个人信息成功');
      }
    };

    // 添加兴趣爱好
    const addHobby = () => {
      if (newHobby.value.trim() && !hobbies.value.includes(newHobby.value.trim())) {
        hobbies.value.push(newHobby.value.trim());
        newHobby.value = '';
      }
    };

    // 删除兴趣爱好
    const removeHobby = (index) => {
      hobbies.value.splice(index, 1);
    };

    // 添加技能
    const addSkill = () => {
      skills.value.push({ name: '', level: '初级' });
    };

    // 删除技能
    const removeSkill = (index) => {
      skills.value.splice(index, 1);
    };

    // 添加教育经历
    const addEducation = () => {
      education.value.push({
        school: '',
        period: '',
        major: '',
        degree: '本科'
      });
    };

    // 删除教育经历
    const removeEducation = (index) => {
      education.value.splice(index, 1);
    };

    // 动态头像样式
    const avatarClass = computed(() => {
      // 可以根据一些条件动态改变头像样式
      return 'avatar-default';
    });

    return {
      isEditing,
      userName,
      studentId,
      className,
      major,
      birthDate,
      hometown,
      politicalStatus,
      email,
      phone,
      website,
      bio,
      userAvatar,
      hobbies,
      newHobby,
      skills,
      education,
      toggleEditMode,
      addHobby,
      removeHobby,
      addSkill,
      removeSkill,
      addEducation,
      removeEducation,
      avatarClass
    };
  }
};
</script>

<style scoped>
/* 全局样式 */
.user-info-container {
  padding: 30px;
  background-color: #f0f2f5;
  min-height: 100vh;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* 头部样式 */
.user-info-header {
  background: linear-gradient(135deg, #3498db, #2980b9);
  color: white;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
  margin-bottom: 30px;
  transition: transform 0.3s ease;
}

.user-info-header:hover {
  transform: translateY(-5px);
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
}

.avatar-container {
  display: flex;
  align-items: center;
}

.avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 32px;
  margin-right: 20px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  transition: all 0.3s ease;
}

.avatar:hover {
  transform: scale(1.05);
}

.avatar-default {
  background-color: #fff;
  color: #3498db;
}

.user-basic {
  margin: 0;
}

.user-basic h2 {
  font-size: 28px;
  margin: 0 0 5px 0;
  color: white;
}

.user-id, .user-class, .user-major {
  font-size: 14px;
  opacity: 0.9;
  margin: 3px 0;
}

.edit-btn {
  background-color: rgba(255, 255, 255, 0.2);
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 25px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  transition: all 0.3s ease;
}

.edit-btn:hover {
  background-color: rgba(255, 255, 255, 0.3);
  transform: translateY(-2px);
}

/* 内容区域样式 */
.user-info-content {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(450px, 1fr));
  gap: 30px;
  margin-bottom: 30px;
}

.info-card {
  background-color: white;
  padding: 25px;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
  transition: all 0.3s ease;
}

.info-card:hover {
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
  transform: translateY(-3px);
}

.info-card.editing {
  border: 1px dashed #3498db;
}

.info-card h3 {
  font-size: 20px;
  color: #2c3e50;
  margin-top: 0;
  margin-bottom: 20px;
  padding-bottom: 15px;
  border-bottom: 2px solid #f0f2f5;
}

.info-item {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
  padding-bottom: 15px;
  border-bottom: 1px solid #f0f2f5;
}

.info-item.full-width {
  grid-column: 1 / -1;
}

.info-item:last-child {
  border-bottom: none;
  margin-bottom: 0;
  padding-bottom: 0;
}

label {
  font-weight: 600;
  color: #7f8c8d;
  margin-bottom: 8px;
  font-size: 14px;
}

span {
  color: #2c3e50;
  font-size: 16px;
  line-height: 1.5;
}

input, textarea, select {
  width: 100%;
  padding: 10px 15px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 16px;
  transition: border 0.3s ease;
  margin-bottom: 10px;
}

input:focus, textarea:focus, select:focus {
  border-color: #3498db;
  outline: none;
  box-shadow: 0 0 0 2px rgba(52, 152, 219, 0.2);
}

textarea {
  min-height: 100px;
  resize: vertical;
}

/* 兴趣爱好样式 */
.hobbies-container {
  margin-top: 15px;
}

.hobby-input {
  display: flex;
  margin-bottom: 15px;
}

.hobby-input input {
  flex: 1;
  margin-right: 10px;
  margin-bottom: 0;
}

.hobby-input button {
  padding: 0 15px;
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}

.hobby-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.hobby-tag {
  background-color: #e8f4fd;
  color: #3498db;
  padding: 5px 10px;
  border-radius: 20px;
  font-size: 14px;
  display: inline-flex;
  align-items: center;
}

.remove-hobby {
  margin-left: 5px;
  cursor: pointer;
  font-weight: bold;
}

/* 技能样式 */
.skills-container {
  margin-top: 15px;
}

.skill-item {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 15px;
  padding-bottom: 15px;
  border-bottom: 1px dashed #eee;
}

.skill-item:last-child {
  border-bottom: none;
}

.skill-name, .skill-level {
  flex: 1;
  min-width: 150px;
}

.skill-actions button {
  padding: 5px 10px;
  background-color: #e74c3c;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.add-skill {
  margin-top: 15px;
  text-align: center;
}

.add-skill button {
  padding: 8px 16px;
  background-color: #2ecc71;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

/* 教育经历样式 */
.education-container {
  margin-top: 15px;
}

.education-item {
  margin-bottom: 20px;
  padding-bottom: 20px;
  border-bottom: 1px dashed #eee;
}

.education-item:last-child {
  border-bottom: none;
}

.edu-school, .edu-period, .edu-major, .edu-degree {
  margin-bottom: 10px;
}

.edu-actions button {
  padding: 5px 10px;
  background-color: #e74c3c;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.add-education {
  margin-top: 15px;
  text-align: center;
}

.add-education button {
  padding: 8px 16px;
  background-color: #2ecc71;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

/* 响应式调整 */
@media (max-width: 768px) {
  .header-content {
    flex-direction: column;
    text-align: center;
  }

  .avatar-container {
    margin-bottom: 20px;
  }

  .user-info-content {
    grid-template-columns: 1fr;
  }

  .skill-name, .skill-level {
    min-width: 100%;
  }
}
</style>