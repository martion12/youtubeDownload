<template>
  <div class="container">
    <!-- 标题部分 -->
    <div class="header">
      <h1>
        <span class="green-text">GreenVideo</span>
        <span class="dark-text">YouTube视频下载</span>
      </h1>
      <p class="subtitle">免费、稳定、速度快、支持1000+海量视频平台的下载</p>
    </div>

    <!-- 下载区域 -->
    <div class="download-area">
      <el-input
        v-model="videoUrl"
        placeholder="请将复制的视频链接粘贴到此处，并点击开始按钮"
        :clearable="true"
        class="url-input"
      >
        <template #append>
          <el-button 
            type="success" 
            :loading="loading"
            @click="handleDownload"
          >
            开始
          </el-button>
        </template>
      </el-input>

      <!-- 视频信息展示 -->
      <div v-if="videoInfo" class="video-info">
        <el-card>
          <div class="info-content">
            <img :src="videoInfo.thumbnail" class="thumbnail">
            <div class="info-text">
              <h3>{{ videoInfo.title }}</h3>
              <p>时长: {{ formatDuration(videoInfo.duration) }}</p>
              <p>观看次数: {{ formatNumber(videoInfo.view_count) }}</p>
              <el-button type="primary" @click="downloadVideo">下载视频</el-button>
            </div>
          </div>
        </el-card>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { ElMessage } from 'element-plus'
import axios from 'axios'

const videoUrl = ref('')
const loading = ref(false)
const videoInfo = ref(null)

const handleDownload = async () => {
  if (!videoUrl.value) {
    ElMessage.warning('请输入视频链接')
    return
  }

  loading.value = true
  try {
    const response = await axios.post('http://localhost:5000/api/video/info', {
      url: videoUrl.value
    })
    videoInfo.value = response.data
    ElMessage.success('获取视频信息成功')
  } catch (error) {
    ElMessage.error(error.response?.data?.error || '获取视频信息失败')
  } finally {
    loading.value = false
  }
}

const downloadVideo = async () => {
  try {
    const response = await axios.post('http://localhost:5000/api/video/download', {
      url: videoUrl.value
    })
    ElMessage.success('开始下载视频')
  } catch (error) {
    ElMessage.error('下载失败')
  }
}

const formatDuration = (seconds) => {
  const hours = Math.floor(seconds / 3600)
  const minutes = Math.floor((seconds % 3600) / 60)
  const remainingSeconds = seconds % 60
  return `${hours ? hours + ':' : ''}${minutes.toString().padStart(2, '0')}:${remainingSeconds.toString().padStart(2, '0')}`
}

const formatNumber = (num) => {
  return new Intl.NumberFormat().format(num)
}
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 40px 20px;
}

.header {
  text-align: center;
  margin-bottom: 40px;
}

.green-text {
  color: #4CAF50;
}

.dark-text {
  color: #333;
}

h1 {
  font-size: 2.5em;
  margin-bottom: 10px;
}

.subtitle {
  color: #666;
  font-size: 1.1em;
}

.download-area {
  margin-top: 30px;
}

.url-input {
  margin-bottom: 20px;
}

.video-info {
  margin-top: 20px;
}

.info-content {
  display: flex;
  gap: 20px;
}

.thumbnail {
  width: 200px;
  height: auto;
  border-radius: 8px;
}

.info-text {
  flex: 1;
}

.info-text h3 {
  margin-top: 0;
}
</style> 