<template>
    <div class="user-info-container">
        <div class="user-info-header">
            <div class="header-decoration"></div>
            <div class="header-content">
                <div class="avatar-container">
                    <!-- 头像容器（包含预览和上传层） -->
                    <div class="avatar-wrapper">
                        <!-- 头像区域（可点击触发上传） -->
                        <div
                            class="avatar"
                            :class="avatarClass"
                            @click="triggerUpload"
                            role="button"
                            tabindex="0"
                            aria-label="更换头像"
                        >
                            <!-- 自定义头像图片 -->
                            <img
                                v-if="userAvatarUrl"
                                :src="userAvatarUrl"
                                class="custom-avatar"
                                alt="用户头像"
                            />
                            <!-- 默认头像图标 -->
                            <span v-else class="icon">{{ userAvatar }}</span>

                            <!-- 悬停时显示的操作层 -->
                            <div class="avatar-overlay">
                                <span class="overlay-text">更换头像</span>
                            </div>
                        </div>

                        <!-- 隐藏的文件选择器 -->
                        <input
                            type="file"
                            id="avatar-upload"
                            class="avatar-upload"
                            accept="image/*"
                            @change="handleAvatarUpload"
                        />

                        <!-- 头像操作按钮组 -->
                        <div class="avatar-actions">
                            <button
                                class="action-btn upload-btn"
                                @click="triggerUpload"
                            >
                                上传头像
                            </button>
                            <button
                                class="action-btn reset-btn"
                                @click="resetAvatar"
                                v-if="userAvatarUrl"
                            >
                                恢复默认
                            </button>
                        </div>
                    </div>

                    <div class="user-basic">
                        <h2 class="user-name">{{ userName }}</h2>
                        <p class="user-id">{{ studentId }}</p>
                        <p class="user-class">{{ className }}</p>
                        <p class="user-major">{{ major }}</p>
                    </div>
                </div>
                <button class="edit-btn" @click="toggleEditMode">
                    <span v-if="!isEditing">编辑信息</span>
                    <span v-if="isEditing">保存</span>
                    <i class="edit-icon" :class="{ 'rotate-icon': isEditing }"
                        >✎</i
                    >
                </button>
            </div>
        </div>

        <!-- 信息内容区域 -->
        <div class="user-info-content">
            <div class="info-card" :class="{ editing: isEditing }">
                <div class="card-header">
                    <h3>基本信息</h3>
                    <div class="card-icon">👤</div>
                </div>
                <div class="info-item">
                    <label>出生日期:</label>
                    <template v-if="isEditing">
                        <input type="date" v-model="birthDate" />
                    </template>
                    <span v-else>{{ birthDate }}</span>
                </div>
                <div class="info-item">
                    <label>籍贯:</label>
                    <template v-if="isEditing">
                        <input
                            type="text"
                            v-model="hometown"
                            placeholder="输入籍贯"
                        />
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

            <div class="info-card" :class="{ editing: isEditing }">
                <div class="card-header">
                    <h3>联系方式</h3>
                    <div class="card-icon">✉️</div>
                </div>
                <div class="info-item">
                    <label>电子邮箱:</label>
                    <template v-if="isEditing">
                        <input
                            type="email"
                            v-model="email"
                            placeholder="输入电子邮箱"
                        />
                    </template>
                    <span v-else>{{ email }}</span>
                </div>
                <div class="info-item">
                    <label>联系电话:</label>
                    <template v-if="isEditing">
                        <input
                            type="tel"
                            v-model="phone"
                            placeholder="输入联系电话"
                        />
                    </template>
                    <span v-else>{{ phone }}</span>
                </div>
                <div class="info-item">
                    <label>个人网站:</label>
                    <template v-if="isEditing">
                        <input
                            type="url"
                            v-model="website"
                            placeholder="输入个人网站"
                        />
                    </template>
                    <span v-else>{{ website || "未设置" }}</span>
                </div>
            </div>

            <div
                class="info-card full-width-card"
                :class="{ editing: isEditing }"
            >
                <div class="card-header">
                    <h3>个人简介</h3>
                    <div class="card-icon">📝</div>
                </div>
                <div class="info-item full-width">
                    <template v-if="isEditing">
                        <textarea
                            v-model="bio"
                            placeholder="输入个人简介"
                            rows="5"
                        ></textarea>
                    </template>
                    <span v-else>{{ bio }}</span>
                </div>
            </div>

            <div
                class="info-card full-width-card"
                :class="{ editing: isEditing }"
            >
                <div class="card-header">
                    <h3>兴趣爱好</h3>
                    <div class="card-icon">🎯</div>
                </div>
                <div class="hobbies-container">
                    <template v-if="isEditing">
                        <div class="hobby-input">
                            <input
                                type="text"
                                v-model="newHobby"
                                placeholder="添加兴趣爱好"
                            />
                            <button @click="addHobby">添加</button>
                        </div>
                    </template>
                    <div class="hobby-tags">
                        <span
                            v-for="(hobby, index) in hobbies"
                            :key="index"
                            class="hobby-tag"
                        >
                            {{ hobby }}
                            <span
                                v-if="isEditing"
                                class="remove-hobby"
                                @click.stop="removeHobby(index)"
                                >×</span
                            >
                        </span>
                    </div>
                </div>
            </div>

            <div
                class="info-card full-width-card"
                :class="{ editing: isEditing }"
            >
                <div class="card-header">
                    <h3>技能特长</h3>
                    <div class="card-icon">🛠️</div>
                </div>
                <div class="skills-container">
                    <div
                        v-for="(skill, index) in skills"
                        :key="index"
                        class="skill-item"
                    >
                        <div class="skill-name">
                            <template v-if="isEditing">
                                <input
                                    type="text"
                                    v-model="skill.name"
                                    placeholder="技能名称"
                                />
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
                            <div class="skill-indicator" v-else>
                                <div
                                    class="indicator-bar"
                                    :style="{
                                        width: getSkillWidth(skill.level),
                                    }"
                                ></div>
                            </div>
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

            <div
                class="info-card full-width-card"
                :class="{ editing: isEditing }"
            >
                <div class="card-header">
                    <h3>教育经历</h3>
                    <div class="card-icon">🎓</div>
                </div>
                <div class="education-container">
                    <div
                        v-for="(edu, index) in education"
                        :key="index"
                        class="education-item"
                    >
                        <div class="edu-school">
                            <template v-if="isEditing">
                                <input
                                    type="text"
                                    v-model="edu.school"
                                    placeholder="学校名称"
                                />
                            </template>
                            <span v-else>{{ edu.school }}</span>
                        </div>
                        <div class="edu-dates">
                            <template v-if="isEditing">
                                <div class="date-inputs">
                                    <input
                                        type="date"
                                        v-model="edu.period_s"
                                        placeholder="入学"
                                    />
                                    <span class="date-separator">-</span>
                                    <input
                                        type="date"
                                        v-model="edu.period_e"
                                        placeholder="毕业"
                                    />
                                </div>
                            </template>
                            <span v-else>
                                {{ edu.period_s }} - {{ edu.period_e }}
                            </span>
                        </div>
                        <div class="edu-major">
                            <template v-if="isEditing">
                                <input
                                    type="text"
                                    v-model="edu.major"
                                    placeholder="专业"
                                />
                            </template>
                            <span v-else>{{ edu.major }}</span>
                        </div>
                        <div class="edu-degree">
                            <template v-if="isEditing">
                                <select v-model="edu.degree">
                                    <option value="本科">本科</option>
                                    <option value="硕士">硕士</option>
                                    <option value="博士">博士</option>
                                    <option value="高中">高中</option>
                                    <option value="初中">初中</option>
                                    <option value="小学">小学</option>
                                </select>
                            </template>
                            <span v-else>{{ edu.degree }}</span>
                        </div>
                        <div v-if="isEditing" class="edu-actions">
                            <button @click="removeEducation(index)">
                                删除
                            </button>
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
import { ref, computed } from "vue";

export default {
    name: "UserInfo",
    setup() {
        // 头像相关数据
        const userAvatarUrl = ref(""); // 自定义头像URL
        const userAvatar = ref("👨‍💻"); // 默认头像emoji

        // 基本信息数据
        const isEditing = ref(false);
        const userName = ref("张三");
        const studentId = ref("20230001");
        const className = ref("计算机科学与技术 2023级");
        const major = ref("计算机科学与技术");
        const birthDate = ref("2005-01-15");
        const hometown = ref("广东省广州市");
        const politicalStatus = ref("团员");
        const email = ref("zhangsan@example.com");
        const phone = ref("13800138000");
        const website = ref("");
        const bio = ref(
            "我是一名计算机科学与技术专业的学生，热爱编程和学习新技术。我对人工智能和大数据分析特别感兴趣，希望未来能在这些领域发展。"
        );
        const hobbies = ref(["编程", "篮球", "音乐", "阅读"]);
        const newHobby = ref("");
        const skills = ref([
            { name: "JavaScript", level: "中级" },
            { name: "Python", level: "初级" },
            { name: "HTML/CSS", level: "高级" },
            { name: "Vue.js", level: "中级" },
        ]);
        const education = ref([
            {
                school: "华南师范大学",
                period_s: "2021-09-01",
                period_e: "2025-06-30",
                major: "计算机科学与技术",
                degree: "本科",
            },
        ]);

        // 头像处理方法 - 修复点击头像无法上传的问题
        const triggerUpload = () => {
            // 直接触发文件选择器点击
            const fileInput = document.getElementById("avatar-upload");
            if (fileInput) {
                fileInput.click();
            }
        };

        const handleAvatarUpload = (e) => {
            const file = e.target.files[0];
            if (file) {
                // 验证文件类型
                if (!file.type.startsWith("image/")) {
                    alert("请选择图片文件（JPG、PNG等格式）");
                    return;
                }

                // 验证文件大小（限制5MB以内）
                if (file.size > 5 * 1024 * 1024) {
                    alert("图片大小不能超过5MB");
                    return;
                }

                // 预览图片
                const reader = new FileReader();
                reader.onload = (event) => {
                    userAvatarUrl.value = event.target.result;
                };
                reader.readAsDataURL(file);

                // 清空输入，允许重复选择同一文件
                e.target.value = "";
            }
        };

        const resetAvatar = () => {
            if (confirm("确定要恢复默认头像吗？")) {
                userAvatarUrl.value = "";
            }
        };

        // 信息编辑方法
        const toggleEditMode = () => {
            isEditing.value = !isEditing.value;
            if (!isEditing.value) {
                console.log("保存个人信息成功");
                // 实际项目中可在此处添加保存到服务器的逻辑
            }
        };

        // 兴趣爱好管理
        const addHobby = () => {
            if (
                newHobby.value.trim() &&
                !hobbies.value.includes(newHobby.value.trim())
            ) {
                hobbies.value.push(newHobby.value.trim());
                newHobby.value = "";
            }
        };

        const removeHobby = (index) => {
            hobbies.value.splice(index, 1);
        };

        // 技能管理
        const addSkill = () => {
            skills.value.push({ name: "", level: "初级" });
        };

        const removeSkill = (index) => {
            skills.value.splice(index, 1);
        };

        // 教育经历管理
        const addEducation = () => {
            education.value.push({
                school: "",
                period_s: "",
                period_e: "",
                major: "",
                degree: "本科",
            });
        };

        const removeEducation = (index) => {
            education.value.splice(index, 1);
        };

        // 技能水平指示器宽度计算
        const getSkillWidth = (level) => {
            const levels = {
                初级: "25%",
                中级: "50%",
                高级: "75%",
                精通: "100%",
            };
            return levels[level] || "0%";
        };

        // 头像样式计算
        const avatarClass = computed(() => {
            return "avatar-gradient";
        });

        return {
            // 头像相关
            userAvatarUrl,
            userAvatar,
            triggerUpload,
            handleAvatarUpload,
            resetAvatar,

            // 基本信息
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

            // 兴趣爱好
            hobbies,
            newHobby,
            addHobby,
            removeHobby,

            // 技能特长
            skills,
            addSkill,
            removeSkill,
            getSkillWidth,

            // 教育经历
            education,
            addEducation,
            removeEducation,

            // 通用方法
            toggleEditMode,
            avatarClass,
        };
    },
};
</script>

<style scoped>
/* 头像相关样式 */
.avatar-wrapper {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 15px;
}

.avatar {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 40px;
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
    transition: all 0.4s ease;
    border: 3px solid rgba(255, 255, 255, 0.2);
    position: relative;
    overflow: hidden;
    cursor: pointer;
    margin: 0;
}

.custom-avatar {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 50%;
}

.avatar-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    transition: opacity 0.3s ease;
    border-radius: 50%;
}

.avatar:hover .avatar-overlay {
    opacity: 1;
}

.overlay-text {
    font-size: 14px;
    font-weight: 500;
    transform: translateY(5px);
    transition: transform 0.3s ease;
}

.avatar:hover .overlay-text {
    transform: translateY(0);
}

.avatar-upload {
    display: none;
}

.avatar-actions {
    display: flex;
    gap: 10px;
    width: 100%;
    max-width: 220px;
    padding: 0 5px;
    box-sizing: border-box;
}

.action-btn {
    padding: 7px 0;
    border-radius: 6px;
    font-size: 13px;
    cursor: pointer;
    transition: all 0.3s ease;
    border: none;
    font-weight: 500;
    flex: 1;
    text-align: center;
}

.upload-btn {
    background: linear-gradient(90deg, #4a6fa5, #36cbcb);
    color: white;
}

.upload-btn:hover {
    box-shadow: 0 4px 12px rgba(74, 111, 165, 0.3);
    transform: translateY(-2px);
}

.reset-btn {
    background-color: #f0f7ff;
    color: #4a6fa5;
    border: 1px solid #d1e0f5;
}

.reset-btn:hover {
    background-color: #e6f0ff;
    transform: translateY(-2px);
}

/* 全局样式 */
.user-info-container {
    padding: 30px;
    background-color: #f7f9fc;
    min-height: 100vh;
    font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
    color: #333;
    line-height: 1.6;
}

.user-info-header {
    position: relative;
    background: linear-gradient(135deg, #4a6fa5 0%, #36cbcb 100%);
    color: white;
    padding: 35px;
    border-radius: 16px;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
    margin-bottom: 30px;
    overflow: hidden;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.user-info-header:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
}

.header-decoration {
    position: absolute;
    top: 0;
    right: 0;
    width: 300px;
    height: 300px;
    background: radial-gradient(
        circle,
        rgba(255, 255, 255, 0.1) 0%,
        rgba(255, 255, 255, 0) 70%
    );
    border-radius: 50%;
    transform: translate(30%, -30%);
    z-index: 0;
}

.header-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    position: relative;
    z-index: 1;
}

.avatar-container {
    display: flex;
    align-items: center;
}

.avatar-gradient {
    background: linear-gradient(
        135deg,
        rgba(255, 255, 255, 0.9),
        rgba(255, 255, 255, 0.7)
    );
    color: #4a6fa5;
}

.avatar:hover {
    transform: scale(1.08) rotate(5deg);
}

.user-basic {
    margin: 0 0 0 20px;
}

.user-basic h2 {
    font-size: 32px;
    margin: 0 0 8px 0;
    color: white;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.user-name,
.user-id,
.user-class,
.user-major {
    font-size: 15px;
    opacity: 0.92;
    margin: 4px 0;
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.edit-btn {
    background-color: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(5px);
    color: white;
    border: none;
    padding: 11px 22px;
    border-radius: 30px;
    cursor: pointer;
    font-size: 15px;
    font-weight: 500;
    transition: all 0.3s ease;
    display: inline-flex;
    align-items: center;
    gap: 8px;
}

.edit-btn:hover {
    background-color: rgba(255, 255, 255, 0.3);
    transform: translateY(-3px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.edit-icon {
    transition: transform 0.3s ease;
}

.rotate-icon {
    transform: rotate(180deg);
}

.user-info-content {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    width: 100%;
}

.full-width-card {
    grid-column: 1 / -1;
}

.info-card {
    background-color: white;
    padding: 25px;
    border-radius: 16px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.03);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.info-card::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: linear-gradient(90deg, #4a6fa5, #36cbcb);
    transform: scaleX(0);
    transform-origin: left center;
    transition: transform 0.3s ease;
}

.info-card:hover::before {
    transform: scaleX(1);
}

.info-card:hover {
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
    transform: translateY(-5px);
}

.info-card.editing {
    border: 1px dashed #36cbcb;
    background-color: #fcfdff;
}

.card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}

.info-card h3 {
    font-size: 19px;
    color: #2c3e50;
    margin-top: 0;
    margin-bottom: 0;
    padding-bottom: 15px;
    position: relative;
    display: flex;
    align-items: center;
    gap: 10px;
}

.info-card h3::after {
    content: "";
    position: absolute;
    bottom: 0;
    left: 0;
    width: 50px;
    height: 3px;
    background: linear-gradient(90deg, #4a6fa5, #36cbcb);
    border-radius: 3px;
}

.card-icon {
    font-size: 22px;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background-color: #f0f7ff;
    color: #4a6fa5;
    display: flex;
    align-items: center;
    justify-content: center;
}

.info-item {
    display: flex;
    flex-direction: column;
    margin-bottom: 22px;
    padding-bottom: 18px;
    border-bottom: 1px solid #f0f2f5;
    transition: all 0.2s ease;
}

.info-item:hover {
    background-color: #fafbff;
    padding-left: 5px;
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
    color: #6c7a89;
    margin-bottom: 8px;
    font-size: 14px;
    display: flex;
    align-items: center;
    gap: 6px;
}

label::before {
    content: "•";
    font-size: 8px;
    color: #4a6fa5;
}

span {
    color: #2c3e50;
    font-size: 16px;
    line-height: 1.6;
}

input,
textarea,
select {
    width: 80%;
    padding: 11px 10px;
    border: 1px solid #e1e5eb;
    border-radius: 8px;
    font-size: 16px;
    transition: all 0.3s ease;
    margin-bottom: 10px;
    background-color: #fcfdff;
}

input:focus,
textarea:focus,
select:focus {
    border-color: #4a6fa5;
    outline: none;
    box-shadow: 0 0 0 3px rgba(74, 111, 165, 0.15);
    transform: translateY(-2px);
}

textarea {
    min-height: 120px;
    resize: vertical;
    line-height: 1.6;
}

.hobbies-container {
    margin-top: 15px;
}

.hobby-input {
    display: flex;
    margin-bottom: 20px;
    gap: 12px;
}

.hobby-input input {
    flex: 1;
    margin-bottom: 0;
}

.hobby-input button {
    padding: 0 20px;
    background: linear-gradient(90deg, #4a6fa5, #36cbcb);
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s ease;
    font-weight: 500;
}

.hobby-input button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(74, 111, 165, 0.3);
}

.hobby-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    padding: 10px 0;
}

.hobby-tag {
    background-color: #f0f7ff;
    color: #4a6fa5;
    padding: 6px 16px;
    border-radius: 20px;
    font-size: 14px;
    display: inline-flex;
    align-items: center;
    transition: all 0.3s ease;
    border: 1px solid transparent;
}

.hobby-tag:hover {
    background-color: #e6f0ff;
    transform: translateY(-2px);
    box-shadow: 0 3px 8px rgba(74, 111, 165, 0.15);
    border-color: #d1e0f5;
}

.remove-hobby {
    margin-left: 8px;
    cursor: pointer;
    font-weight: bold;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background-color: rgba(74, 111, 165, 0.1);
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 12px;
    transition: all 0.2s ease;
}

.remove-hobby:hover {
    background-color: #e74c3c;
    color: white;
}

.skills-container {
    margin-top: 15px;
}

.skill-item {
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
    margin-bottom: 20px;
    padding-bottom: 20px;
    border-bottom: 1px dashed #f0f2f5;
    align-items: center;
}

.skill-item:last-child {
    border-bottom: none;
}

.skill-name,
.skill-level {
    flex: 1;
    min-width: 150px;
}

.skill-level {
    position: relative;
}

.skill-indicator {
    width: 100%;
    height: 8px;
    background-color: #f0f2f5;
    border-radius: 4px;
    margin-top: 6px;
    overflow: hidden;
}

.indicator-bar {
    height: 100%;
    background: linear-gradient(90deg, #4a6fa5, #36cbcb);
    border-radius: 4px;
    transition: width 0.6s ease;
}

.skill-actions button {
    padding: 6px 12px;
    background-color: #fdecea;
    color: #e74c3c;
    border: 1px solid #fcd9cf;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.skill-actions button:hover {
    background-color: #e74c3c;
    color: white;
}

.add-skill {
    margin-top: 15px;
    text-align: center;
}

.add-skill button {
    padding: 9px 18px;
    background: linear-gradient(90deg, #4a6fa5, #36cbcb);
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.3s ease;
    font-weight: 500;
}

.add-skill button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(74, 111, 165, 0.3);
}

.education-container {
    margin-top: 15px;
}

.education-item {
    display: grid;
    grid-template-columns: 2fr 2fr 2fr 1.5fr auto;
    gap: 20px;
    align-items: center;
    margin-bottom: 20px;
    padding: 15px 0;
    border-bottom: 1px dashed #f0f2f5;
}

.education-item:last-child {
    border-bottom: none;
}

.edu-dates {
    display: flex;
    align-items: center;
}

.date-inputs {
    display: flex;
    align-items: center;
    gap: 12px;
    width: 100%;
    padding: 0;
    margin: 0;
    border-bottom: none;
}

.date-inputs input {
    width: 100%;
    min-width: 120px;
}

.edu-major,
.edu-school {
    width: 100%;
}

.edu-degree {
    width: 100%;
}

.edu-actions {
    white-space: nowrap;
}

.date-separator {
    color: #6c7a89;
    font-weight: 500;
    padding: 0 2px;
}

.edu-actions button {
    padding: 6px 12px;
    background-color: #fdecea;
    color: #e74c3c;
    border: 1px solid #fcd9cf;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.edu-actions button:hover {
    background-color: #e74c3c;
    color: white;
}

.add-education {
    margin-top: 15px;
    text-align: center;
}

.add-education button {
    padding: 9px 18px;
    background: linear-gradient(90deg, #4a6fa5, #36cbcb);
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.3s ease;
    font-weight: 500;
}

.add-education button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(74, 111, 165, 0.3);
}

/* 响应式调整 */
@media (max-width: 992px) {
    .user-info-content {
        grid-template-columns: 1fr;
    }
}

@media (max-width: 768px) {
    .header-content {
        flex-direction: column;
        text-align: center;
    }

    .avatar-container {
        margin-bottom: 25px;
        flex-direction: column;
    }

    .user-basic {
        margin: 20px 0 0 0;
    }

    .avatar {
        margin-right: 0;
        margin-bottom: 15px;
    }

    .edit-btn {
        margin-top: 15px;
        width: 100%;
        justify-content: center;
    }

    .skill-name,
    .skill-level {
        min-width: 100%;
    }

    .user-info-container {
        padding: 20px 15px;
    }

    .info-card {
        padding: 20px 15px;
    }

    .education-item {
        grid-template-columns: 1fr 1fr;
        gap: 15px;
    }
}

@media (max-width: 480px) {
    .education-item {
        grid-template-columns: 1fr;
    }
    .date-inputs input {
        width: 45%;
    }
}
</style>
