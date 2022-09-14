<template>
  <div class="q-pa-md " >
   
    <q-card class="my-card ">
      <q-card-section>
        <q-form
        @submit="onSubmit"
      
      class="q-gutter-md form"
    >  
    
      <q-input
        filled
        v-model="form.name"
        label="Nombre *"
        hint="Nombre del juego"
        lazy-rules
        :rules="[ val => val && val.length > 0 || 'Escribe un nombre']"
      />
      <q-input
        filled
        type="textarea"
        v-model="form.description"
        label="Descripción *"
        hint="Descripción del juego"
        lazy-rules
        :rules="[ val => val && val.length > 0 || 'Escribe una descripción']"
      />
      <q-input
        filled
        v-model="form.category"
        label="Categoria"
        hint="Categoria del juego"
        
      />
      
      <q-input
        filled
        type="number"
        v-model="form.size"
        label="Peso *"
        lazy-rules
        :rules="[
          val => val !== null && val !== '' || 'Especifica un peso',
          
        ]"
      />
      <q-select v-model="form.measure_unit" :options="um_opt" label="Unidad de medida" emit-value
        map-options />

      <q-input
        filled
        type="number"
        v-model="form.price"
        label="Precio  *"
        lazy-rules
        :rules="[
          val => val !== null && val !== '' || 'Especifica un precio',
          
        ]"
      />
      <!-- <q-file outlined v-model="form.image">
        <template v-slot:prepend>
          <q-icon name="attach_file" />
        </template>
      </q-file> -->
      <q-select v-model="form.plataform" :options="plataform_opt" label="Plataforma" emit-value
        map-options />
      

      <div>
        <q-btn label="Submit" type="submit" color="primary"/>
        <q-btn label="Reset" type="reset" color="primary" flat class="q-ml-sm" />
      </div>
    </q-form>
      </q-card-section>
    </q-card>

  

  </div>
</template>

<script>
import { useQuasar } from 'quasar'
import { ref ,onMounted,defineComponent} from 'vue'
import { useRouter } from 'vue-router'
import gameService from 'src/services/game'
import plataformService from 'src/services/plataformas'
import umService from 'src/services/medidas'

export default defineComponent( {
  name : 'GameForm',
  setup () {
    const $q = useQuasar()
    const router = useRouter()
    const {postGame} = gameService()
    const {listPlataform} = plataformService()
    const {listUM} = umService()
    
    const plataform_opt = ref([])
    const um_opt = ref([])
    
    onMounted(() => {
      GetPlataform(),
      GetUM()
    })
    const GetPlataform = async () => {
      try {
        const  {data}  = await listPlataform()
        plataform_opt.value = data.map(function(obj){
          var rObj = {};
          rObj['label'] = obj.name;
          rObj['value'] = obj.uuid;
          return rObj;
        });
      } catch (error) {
        console.error(error)
      }
    }
    const GetUM = async () => {
      try {
        const  {data}  = await listUM()
        um_opt.value = data.map(function(obj){
          var rObj = {};
          rObj['label'] = obj.name;
          rObj['value'] = obj.uuid;
          return rObj;
        });
      } catch (error) {
        console.error(error)
      }
    }

    const form = ref({
      name: '',
      description:'',
      size:'',
      category:'',
    
      price:'',
      plataform:'',
      measure_unit:'',

    })

    const onSubmit = async () => {
      try {
        await postGame(form.value)
        $q.notify({
            message: 'El juego se ha creado correctamente.',
            type: 'positive',
          })
        router.push('/')  
      } catch (error) {
        console.error(error)
      }
    }

    return {
    
      form,
      plataform_opt,
      um_opt,
      onSubmit,
    }
  }
})
</script>


  