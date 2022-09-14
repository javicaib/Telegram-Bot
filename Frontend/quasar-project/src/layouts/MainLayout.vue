<template>

  <q-layout view="lHh Lpr lff">
    <q-header elevated class="bg-cyan-8">
      <q-toolbar>
        <q-toolbar-title>Auroradon Project</q-toolbar-title>
        <q-btn flat @click="drawer = !drawer" round dense icon="menu" />
      </q-toolbar>
    </q-header>

    <q-drawer v-model="drawer" show-if-above :width="200" :breakpoint="400">
      <q-scroll-area style="height: calc(100% - 150px); margin-top: 150px; border-right: 1px solid #ddd">
        <q-list padding>
          <q-item clickable v-ripple to="/"  exact>
            <q-item-section avatar>
              <q-icon name="view_list" />
            </q-item-section>

            <q-item-section>
              Listado
            </q-item-section>
          </q-item>

          <q-item  clickable v-ripple excat to="game-form" exact>
            <q-item-section avatar>
              <q-icon name="add" />
            </q-item-section>

            <q-item-section>
              Nuevo Juego
            </q-item-section>
          </q-item>

          
        </q-list>
      </q-scroll-area>

      <q-img class="absolute-top" src="../assets/material.png" style="height: 150px">
        <div class="absolute-bottom bg-transparent">
          <q-avatar size="56px" class="q-mb-sm">
            <img src="../assets/avatar.jpg">
          </q-avatar>
          <div class="text-weight-bold">Javier A. Roque</div>
          <div>@javicaib</div>
        </div>
      </q-img>
    </q-drawer>

    <q-page-container>
      <q-page padding>
        <router-view />
      </q-page>
    </q-page-container>
  </q-layout>

</template>
<script>
import { ref } from 'vue'

export default {
  setup() {
    return {
      drawer: ref(false)
    }
  }
}
</script>