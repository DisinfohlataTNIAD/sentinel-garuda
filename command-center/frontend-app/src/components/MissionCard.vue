<template>
  <div class="mission-card">
    <h3>{{ mission.mission_type }}</h3>
    <p><strong>Lokasi:</strong> {{ mission.location }}</p>
    <p><strong>Tujuan:</strong> {{ mission.objective }}</p>
    <button @click="startMission">Mulai Misi</button>
  </div>
</template>

<script>
export default {
  props: {
    mission: Object
  },
  methods: {
    startMission() {
      this.$emit('start-mission', this.mission);
    }
  }
};
</script>

<style scoped>
.mission-card {
  padding: 15px;
  background-color: #f9f9f9;
  border-radius: 8px;
  margin-bottom: 10px;
}
button {
  background-color: #008CBA;
  color: white;
  padding: 10px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background-color: #006F8E;
}
</style>
