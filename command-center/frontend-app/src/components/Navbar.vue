<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <a href="/" class="logo">Sentinel-Garuda</a>
    </div>
    <ul class="navbar-links">
      <li><a href="/">Beranda</a></li>
      <li><a href="/missions">Misi</a></li>
      <li><a href="/profile">Profil</a></li>
      <li><a href="/about">Tentang</a></li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: "Navbar"
};
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #343a40;
  padding: 15px 30px;
  color: white;
}

.navbar-brand .logo {
  font-size: 1.5em;
  color: white;
  text-decoration: none;
}

.navbar-links {
  list-style: none;
  display: flex;
}

.navbar-links li {
  margin-left: 20px;
}

.navbar-links a {
  color: white;
  text-decoration: none;
  font-size: 1.1em;
}

.navbar-links a:hover {
  text-decoration: underline;
}
</style>
