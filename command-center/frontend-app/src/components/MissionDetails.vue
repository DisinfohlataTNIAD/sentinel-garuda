<template>
  <div class="mission-details">
    <div v-if="mission">
      <h2>{{ mission.mission_type }}</h2>
      <p><strong>Lokasi:</strong> {{ mission.location }}</p>
      <p><strong>Tujuan:</strong> {{ mission.objective }}</p>
      <p><strong>Status:</strong> {{ mission.status }}</p>

      <div v-if="mission.steps && mission.steps.length > 0">
        <h3>Langkah-langkah Operasi:</h3>
        <ul>
          <li v-for="(step, index) in mission.steps" :key="index">{{ step }}</li>
        </ul>
      </div>

      <button @click="startMission" :disabled="isMissionStarted">Mulai Misi</button>
      <p v-if="isMissionStarted">Misi sudah dimulai!</p>
    </div>
    <div v-else>
      <p>Loading mission details...</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    mission: Object
  },
  data() {
    return {
      isMissionStarted: false
    };
  },
  methods: {
    startMission() {
      this.isMissionStarted = true;
      // Emit event to parent to update mission status
      this.$emit('mission-started', this.mission.id);
    }
  }
};
</script>

<style scoped>
.mission-details {
  padding: 20px;
  background-color: #f4f4f4;
  border-radius: 8px;
}

button {
  background-color: #007bff;
  color: white;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:disabled {
  background-color: #d6d6d6;
  cursor: not-allowed;
}

button:hover {
  background-color: #0056b3;
}
</style>
