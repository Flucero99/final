// ------------------------------------------------------ Declaraciones
const input_ingresar = document.getElementById("ingresar-tarea");
const lista_tareas = document.getElementById("lista-tareas");
const boton_iniciar_sesion = document.getElementById("iniciar-sesion");
const botones_completar = document.querySelectorAll("button.completar");
const boton_agregar = document.querySelector(
  "#contenedor-todo > button.agregar"
);
// ------------------------------------------------------ Funciones

function agregar_tarea() {
  // &#128465; -> Basurero y &#10003; -> Check mark
  if (input_ingresar.value) {
    const [tarea, texto] = [
      document.createElement("div"),
      document.createElement("p"),
    ];
    const [boton_borrar, boton_check] = [
      document.createElement("button"),
      document.createElement("button"),
    ];
    boton_borrar.setAttribute("type", "submit");
    boton_check.setAttribute("type", "submit");
    boton_borrar.classList.add("borrar");
    boton_check.classList.add("completar");
    tarea.classList.add("tarea");

    boton_borrar.innerHTML = `&#128465;`;
    boton_check.innerHTML = "&#10003;";
    texto.innerText = input_ingresar.value;

    tarea.appendChild(texto);
    tarea.appendChild(boton_check);
    tarea.appendChild(boton_borrar);
    lista_tareas.appendChild(tarea);
    input_ingresar.value = "";

    listener_boton_borrar(boton_borrar);
    listener_boton_completar(boton_check);
    // tarea.classList.add("tarea")
    // console.log(tarea)
    // console.log(input_ingresar.value);
  }
  return 0;
}

function completar_tarea(e) {
  let tarea = e.target.parentNode;
  let texto = e.target.previousElementSibling;
  texto.classList.toggle("completada");
  tarea.classList.toggle("completada");
  // console.log(tarea);
  return 0;
}

function borrar_tarea(e) {
  let tarea = e.target.parentNode;
  tarea.remove();
  return 0;
}

function expandir_usuarios() {
  let aside = document.querySelector("aside");
  let nada_1 = document.querySelector(".nada-1");
  let nada_2 = document.querySelector(".nada-2");
  aside.classList.toggle("colapsado");
  nada_1.classList.toggle("colapsado");
  nada_2.classList.toggle("colapsado");
  return 0;
}

// ------------------------------------------------------ Listeners
function listener_input() {
  input_ingresar.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
      agregar_tarea();
    }
  });
  return 0;
}

function listener_boton_agregar() {
  boton_agregar.addEventListener("click", agregar_tarea);
  return 0;
}

function listener_boton_completar(boton_check) {
  boton_check.addEventListener("click", completar_tarea);
  return 0;
}
function listener_boton_completar_todos() {
  for (const boton_check of botones_completar) {
    boton_check.addEventListener("click", completar_tarea);
  }
  return 0;
}

function listener_boton_borrar(boton_borrar) {
  boton_borrar.addEventListener("click", borrar_tarea);
  return 0;
}

function listener_boton_iniciar_sesion() {
  boton_iniciar_sesion.addEventListener("click", expandir_usuarios);
  return 0;
}

// --------------------------------------------------------------------------------- Principal

function main() {
  try {
    // listener_input();
    // listener_boton_agregar();
    listener_boton_completar_todos();
  } catch {}
  try {
    listener_boton_iniciar_sesion();
  } catch {}
  // console.log(boton_agregar);
  return 0;
}

main();
