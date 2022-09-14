<template>
  <div class="q-pa-md">
    <q-table title="Listado de juegos" :rows="games" :columns="columns" :visible-columns="visibleColumns" row-key="id"
      :filter="filter" binary-state-sort>
      <template v-slot:top>
        <q-btn color="primary" label="Nuevo juego" to="game-form" />
      </template>
      <template v-slot:top-right>
        <q-input borderless dense debounce="300" v-model="filter" placeholder="Buscar">
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>
      </template>
      <template v-slot:body-cell-actions="props">
        <q-td :props="props" class=" q-gutter-sm">
          <q-btn icon="visibility" color="light-blue-8" glossy dense>
            <q-tooltip class="bg-light-blue-8">Ver detalles</q-tooltip>
          </q-btn>
          <q-btn icon="edit" color="amber" glossy dense>
            <q-tooltip class="bg-amber">Editar</q-tooltip>
          </q-btn>
          <q-btn icon="delete" color="negative" glossy dense @click="DelGames(props.row.uuid)">
            <q-tooltip class="bg-negative">Eliminar</q-tooltip>
          </q-btn>


        </q-td>
      </template>


    </q-table>
  </div>
</template>
<script>
import { defineComponent, onMounted, ref } from 'vue'
import { useQuasar } from 'quasar'
import gameService from 'src/services/game'


export default defineComponent({
  name: 'IndexPage',
  setup() {
    const $q = useQuasar()
    const { listGame, removeGame } = gameService()
    const games = ref([])

    const columns = [
      { name: 'uuid', label: 'ID', field: 'uuid', sortable: true, align: 'left' },
      { name: 'name', label: 'Nombre', field: 'name', sortable: true, align: 'left' },
      { name: 'plataform', label: 'Plataforma', field: 'plataform', sortable: false, align: 'left' },
      { name: 'category', label: 'Categoria', field: 'category', sortable: false, align: 'left' },
      { name: 'size', label: 'Peso', field: 'size', sortable: false, align: 'left' },
      /*{ name: 'description',  label: 'Descripción', field: 'description', sortable: false ,align:'left'},*/
      { name: 'price', label: 'Precio $', field: 'price', sortable: false, align: 'left' },
      { name: 'actions', field: 'actions', label: 'Acciones', sortable: false, align: 'center' },
    ]
    const pagination = ref({
      sortBy: 'desc',
      descending: false,
      page: 1,
      rowsPerPage: 3,
      rowsNumber: 10
    })


    onMounted(() => {
      GetGames()

    })
    const GetGames = async () => {
      try {
        const { data } = await listGame()
        games.value = data
      } catch (error) {
        console.error(error)
      }
    }
    const DelGames = async (id) => {
      try {

        $q.dialog({
          title: 'Eliminación',
          message: 'En verdad deseas borrar este juego?',
          ok: {
            push: true
          },
          cancel: {
            push: true,
            color: 'negative',
            message: 'Cancelar'
          },
          persistent: true
        }).onOk(async () => {
          await removeGame(id)
          $q.notify({
            message: 'El juego se ha borrado correctamente.',
            type: 'positive',
          })
          GetGames()
        })






      } catch (error) {
        $q.notify({
          message: 'Ha ocurrido un error.',
          type: 'negative',
        })
      }
    }
    return {
      visibleColumns: ref(['name', 'price', 'actions', 'category', 'plataform', 'size']),
      games,
      columns,
      filter: ref(''),
      selected: ref([]),
      DelGames,

    }
  }
})
</script>
