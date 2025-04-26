<template>
  <div id="app">
    <header>
      <h1>Sentinel-Garuda: Sistem Simulasi Operasi Intelijen</h1>
    </header>
    <main>
      <section>
        <h2>Simulasi Misi</h2>
        <div v-if="loading" class="loader">Loading...</div>
        <div v-else>
          <div class="mission-details">
            <h3>{{ mission.mission_type }}</h3>
            <p><strong>Lokasi:</strong> {{ mission.location }}</p>
            <p><strong>Tujuan:</strong> {{ mission.objective }}</p>
            <p><strong>Kehadiran Musuh:</strong> {{ mission.enemy_presence }}</p>
            <p><strong>Sumber Daya:</strong> {{ mission.resources.join(', ') }}</p>
            <p><strong>Durasi Misi:</strong> {{ mission.timeline.estimated_duration_hours }} jam</p>
            <button @click="startSimulation">Mulai Simulasi</button>
          </div>
          <div v-if="simulationResult" class="simulation-result">
            <h3>Hasil Simulasi:</h3>
            <p>{{ simulationResult }}</p>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      loading: true,
      mission: {},
      simulationResult: null,
    };
  },
  mounted() {
    // Memuat data misi dari API atau file
    this.loadMissionData();
  },
  methods: {
    // Fungsi untuk memuat data misi (misalnya dari file JSON atau API)
    async loadMissionData() {
      // Ini adalah contoh data misi yang diambil dari file JSON atau API
      // Data misi ini bisa diganti dengan data nyata dari backend
      const missionData = {
        "mission_type": "Operasi Intelijen",
        "location": "Timur Laut Indonesia",
        "objective": "Menangkap terduga jaringan teroris",
        "enemy_presence": "Sedikit",
        "resources": ["Pasukan Khusus", "Dron Pengintai", "Intelijen Satelit", "Tim Medis"],
        "timeline": {
          "start_date": "2025-05-01T00:00:00",
          "end_date": "2025-05-10T23:59:59",
          "estimated_duration_hours": 240
        }
      };

      // Simulasikan waktu pemuatan data
      setTimeout(() => {
        this.mission = missionData;
        this.loading = false;
      }, 1000);
    },

    // Fungsi untuk memulai simulasi misi
    startSimulation() {
      // Menjalankan simulasi dengan hasil acak
      const simulationOutcome = this.simulateMissionOutcome();
      this.simulationResult = simulationOutcome;
    },

    // Fungsi untuk mensimulasikan hasil misi berdasarkan kondisi acak
    simulateMissionOutcome() {
      const outcomes = [
        "Keberhasilan Penuh: Misi berjalan lancar tanpa kendala.",
        "Keberhasilan Terbatas: Misi berhasil tetapi ada kerugian minimal.",
        "Kegagalan: Musuh terlalu kuat dan misi gagal.",
        "Misi Dibatalkan: Kondisi cuaca dan medan tidak memungkinkan untuk melanjutkan."
      ];

      // Pilih hasil secara acak
      const randomIndex = Math.floor(Math.random() * outcomes.length);
      return outcomes[randomIndex];
    }
  }
};
</script>

<style scoped>
#app {
  font-family: 'Arial', sans-serif;
  text-align: center;
}

header {
  background-color: #002d72;
  color: white;
  padding: 10px 0;
}

h1 {
  margin: 0;
}

main {
  padding: 20px;
}

.mission-details {
  background-color: #f0f0f0;
  padding: 20px;
  margin: 20px 0;
  border-radius: 8px;
}

button {
  background-color: #0066cc;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #004d99;
}

.simulation-result {
  margin-top: 20px;
  padding: 15px;
  background-color: #e7f7e7;
  border: 2px solid #4CAF50;
  border-radius: 8px;
}

.loader {
  font-size: 20px;
  color: #333;
}
</style>
