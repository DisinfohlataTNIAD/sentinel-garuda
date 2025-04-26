import json
import random
import time

class SimulationGenerator:
    def __init__(self, scenario_file):
        """
        Inisialisasi dengan file skenario.
        :param scenario_file: Path ke file JSON yang berisi skenario.
        """
        self.scenario_file = scenario_file
        self.scenario = self.load_scenario()

    def load_scenario(self):
        """
        Memuat skenario dari file JSON.
        :return: Data skenario dalam bentuk dictionary.
        """
        try:
            with open(self.scenario_file, 'r') as f:
                scenario_data = json.load(f)
            return scenario_data
        except FileNotFoundError:
            print(f"File {self.scenario_file} tidak ditemukan!")
            return None
        except json.JSONDecodeError:
            print(f"File {self.scenario_file} tidak valid!")
            return None

    def display_scenario(self):
        """
        Menampilkan detail skenario yang dimuat.
        """
        if self.scenario:
            print("Skenario yang Dimuat:")
            print(json.dumps(self.scenario, indent=4))
        else:
            print("Tidak ada skenario untuk ditampilkan.")

    def generate_mission(self):
        """
        Membuat misi berdasarkan skenario yang dimuat.
        :return: Deskripsi misi.
        """
        if not self.scenario:
            return "Tidak ada skenario yang dapat dihasilkan."

        mission_type = self.scenario.get("mission_type", "Operasi Umum")
        location = self.scenario.get("location", "Lokasi Tidak Diketahui")
        objective = self.scenario.get("objective", "Tujuan Tidak Diketahui")
        enemy_presence = random.choice(self.scenario.get("enemy_presence", ["Tidak ada", "Sedikit", "Banyak"]))
        resources = self.scenario.get("resources", ["Sumber Daya Tidak Diketahui"])

        mission_description = f"""
        Misi: {mission_type}
        Lokasi: {location}
        Tujuan: {objective}
        Kehadiran Musuh: {enemy_presence}
        Sumber Daya: {', '.join(resources)}
        """

        return mission_description

    def execute_simulation(self):
        """
        Menjalankan simulasi misi dengan menghasilkan beberapa hasil acak untuk menilai kemungkinan hasil dari operasi.
        :return: Hasil simulasi.
        """
        mission = self.generate_mission()
        print("\nMisi yang Dihasilkan:")
        print(mission)
        
        # Simulasi hasil misi dengan probabilitas berdasarkan kondisi musuh
        enemy_presence = self.scenario.get("enemy_presence", ["Tidak ada"])
        enemy_status = random.choice(enemy_presence)

        if enemy_status == "Banyak":
            mission_result = "Kegagalan: Musuh terlalu kuat."
        elif enemy_status == "Sedikit":
            mission_result = "Keberhasilan dengan kerugian minimal."
        else:
            mission_result = "Keberhasilan penuh: Musuh tidak ada."

        print("\nHasil Simulasi Misi:")
        print(mission_result)

    def run(self):
        """
        Menjalankan simulasi sepenuhnya.
        """
        self.display_scenario()
        time.sleep(2)  # Delay untuk efek dramatis
        self.execute_simulation()


if __name__ == "__main__":
    # Inisialisasi simulator dengan file skenario
    scenario_file = 'wargame/scenarios/sample_scenario.json'
    simulation = SimulationGenerator(scenario_file)
    
    # Menjalankan simulasi
    simulation.run()
      
