<template>
  <div class="video-container">
    <!-- 标题和提示信息 -->
    <div class="header">
      <h1>GreenVideo<span>YouTube</span>视频下载</h1>
      <p class="subtitle">免费、稳定、速度快、支持1000+海量视频平台的下载</p>
    </div>

    <!-- 输入框和按钮 -->
    <div class="input-group">
      <input 
        v-model="videoUrl" 
        type="text" 
        placeholder="https://www.youtube.com/watch?v=..."
        class="url-input"
      >
      <button @click="getVideoInfo" class="start-btn">开始</button>
    </div>

    <!-- 成功提示 -->
    <div v-if="success" class="success-tip">
      <span class="icon">✓</span>
      获取视频信息成功
    </div>

    <!-- 视频信息展示 -->
    <div v-if="videoInfo" class="video-info">
      <div class="info-item">
        <img :src="videoInfo.thumbnail" alt="视频封面" class="thumbnail">
        <div class="details">
          <h3>{{ videoInfo.title }}</h3>
          <p>{{ videoInfo.description }}</p>
          <div class="meta">
            <span>时长: {{ videoInfo.duration }}</span>
            <span>作者: {{ videoInfo.author }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      videoUrl: '',
      videoInfo: null,
      success: false
    }
  },
  methods: {
    async getVideoInfo() {
      try {
        const response = await fetch('http://localhost:5000/api/video/info', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ url: this.videoUrl })
        });
        
        const data = await response.json();
        this.videoInfo = data;
        this.success = true;
      } catch (error) {
        console.error('获取视频信息失败:', error);
        this.success = false;
      }
    },
    formatViews(views) {
      if (views >= 10000) {
        return `${(views / 10000).toFixed(1)}万次观看`
      }
      return `${views}次观看`
    }
  }
}
</script>

<style scoped>
.video-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.header {
  text-align: center;
  margin-bottom: 30px;
}

.header h1 span {
  color: #333;
}

.input-group {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.url-input {
  flex: 1;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.start-btn {
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.success-tip {
  background-color: #f0f9eb;
  color: #67c23a;
  padding: 10px;
  border-radius: 4px;
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.video-info {
  border: 1px solid #eee;
  border-radius: 8px;
  padding: 15px;
}

.info-item {
  display: flex;
  gap: 20px;
}

.thumbnail {
  width: 200px;
  height: 150px;
  object-fit: cover;
  border-radius: 4px;
}

.details {
  flex: 1;
}

.meta {
  display: flex;
  gap: 20px;
  color: #666;
  margin-top: 10px;
}
</style> 