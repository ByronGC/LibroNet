import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from hashTableStr import libros
from hashTableInt import clientes
from categorias import categorias
from clasePedido import Pedido

def abrir_ventana_admin():
    global treeview_libros

    ventana_admin = tk.Toplevel(ventana_principal)
    ventana_admin.title("Admin")
    ventana_admin.geometry("1000x700")

    # Treeview de libros
    treeview_libros = ttk.Treeview(ventana_admin, column=('Nombre','Autor','Año','Genero','Cantidad'))
    treeview_libros.heading('#0', text='Nombre')
    treeview_libros.heading('#1', text='Autor')
    treeview_libros.heading('#2', text='Año')
    treeview_libros.heading('#3', text='Genero')
    treeview_libros.heading('#4', text='Cantidad')

    def clear():
        for item in treeview_libros.get_children():
            treeview_libros.delete(item)

    def ver_libros():
        ct = 0
        clear()
        if ct == 20:
            return
        else:
            for i in libros.arr:
                if i == None:
                    continue
                actual = i.head
                while actual:
                    treeview_libros.insert('', 'end', text=actual.key.nombre, values=(actual.key.autor, actual.key.year, actual.key.genero, actual.key.cantidad))
                    actual = actual.next
                    ct += 1

    ver_libros()

    def agregar_libro():
        nombre = entry_nombre.get()
        autor = entry_autor.get()
        año = entry_anio.get()
        genero = entry_genero.get()
        cantidad = entry_cantidad.get()
        
        if nombre != '' and autor != '' and año != '' and genero != '' and cantidad != '':
            libros.add(nombre, autor, año, genero, int(cantidad))
            treeview_libros.insert('', 'end', text=nombre, values=(autor, año, genero, cantidad))
        
        entry_nombre.delete(0, 'end')
        entry_autor.delete(0, 'end')
        entry_anio.delete(0, 'end')
        entry_genero.delete(0, 'end')
        entry_cantidad.delete(0, 'end')

    def editar_libro():
        try:
            entry_nombre.delete(0, 'end')
            entry_autor.delete(0, 'end')
            entry_anio.delete(0, 'end')
            entry_genero.delete(0, 'end')
            entry_cantidad.delete(0, 'end')
            
            nombre = treeview_libros.item(treeview_libros.selection())['text']
            autor = treeview_libros.item(treeview_libros.selection())['values'][0]
            año = treeview_libros.item(treeview_libros.selection())['values'][1]
            genero = treeview_libros.item(treeview_libros.selection())['values'][2]
            cantidad = treeview_libros.item(treeview_libros.selection())['values'][3]
            
            entry_nombre.insert(0, nombre)
            entry_autor.insert(0, autor)
            entry_anio.insert(0, año)
            entry_genero.insert(0, genero)
            entry_cantidad.insert(0, cantidad)
            
        except:
            pass

    def guardar_datos():
        nombre = entry_nombre.get()
        autor = entry_autor.get()
        año = entry_anio.get()
        genero = entry_genero.get()
        cantidad = entry_cantidad.get()
        
        if nombre != '' and autor != '' and año != '' and genero != '' and cantidad != '':
            nombre_actual = treeview_libros.item(treeview_libros.selection())['text']
            fila_actual = libros.find(nombre_actual).fila
            libros.remove(nombre_actual)
            libros.add(nombre, autor, año, genero, int(cantidad))
            libros.find(nombre).fila = fila_actual
            pedido_atendido = libros.find(nombre).atender_fila()
            
            treeview_libros.item(treeview_libros.selection(), text=nombre)
            treeview_libros.item(treeview_libros.selection(), values=(autor, año, genero, cantidad))
            
            entry_nombre.delete(0, 'end')
            entry_autor.delete(0, 'end')
            entry_anio.delete(0, 'end')
            entry_genero.delete(0, 'end')
            entry_cantidad.delete(0, 'end')

    def eliminar_libro():
        nombre_actual = treeview_libros.item(treeview_libros.selection())['text']
        libros.remove(nombre_actual)
        treeview_libros.delete(treeview_libros.selection())

    def ciencia_ficcion():
        clear()
        actual = categorias.cienciaFiccion.head
        while actual:                        
            treeview_libros.insert('', 'end', text=libros.find(actual.key).nombre, values=(libros.find(actual.key).nombre, libros.find(actual.key).year, libros.find(actual.key).genero, libros.find(actual.key).cantidad))
            actual = actual.next

    def fantasia():
        clear()
        actual = categorias.fantasia.head
        while actual:                        
            treeview_libros.insert('', 'end', text=libros.find(actual.key).nombre, values=(libros.find(actual.key).nombre, libros.find(actual.key).year, libros.find(actual.key).genero, libros.find(actual.key).cantidad))
            actual = actual.next

    def romance():
        clear()
        actual = categorias.romance.head
        while actual:                        
            treeview_libros.insert('', 'end', text=libros.find(actual.key).nombre, values=(libros.find(actual.key).nombre, libros.find(actual.key).year, libros.find(actual.key).genero, libros.find(actual.key).cantidad))
            actual = actual.next

    def poesia():
        clear()
        actual = categorias.poesia.head
        while actual:                        
            treeview_libros.insert('', 'end', text=libros.find(actual.key).nombre, values=(libros.find(actual.key).nombre, libros.find(actual.key).year, libros.find(actual.key).genero, libros.find(actual.key).cantidad))
            actual = actual.next

    def ficcion():
        clear()
        actual = categorias.ficcion.head
        while actual:                        
            treeview_libros.insert('', 'end', text=libros.find(actual.key).nombre, values=(libros.find(actual.key).nombre, libros.find(actual.key).year, libros.find(actual.key).genero, libros.find(actual.key).cantidad))
            actual = actual.next

    def buscar_libro():        
        nombre = entry_buscar_libro_admin.get()
        if libros.find(nombre):
            clear()
            treeview_libros.insert('', 'end', text=libros.find(nombre).nombre, values=(libros.find(nombre).nombre, libros.find(nombre).year, libros.find(nombre).genero, libros.find(nombre).cantidad))
            entry_buscar_libro_admin.delete(0, 'end')
        else:
            pass

    def revisar():
        libros.printTable()

    # Establecer estilo
    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 14, "bold"))
    style.configure("TButton", font=("Arial", 12), padding=10)

    # Frame principal
    frame_principal = ttk.Frame(ventana_admin)
    frame_principal.pack(pady=10)

    # Barra de texto y etiquetas
    frame_barra_texto = ttk.Frame(frame_principal)
    frame_barra_texto.pack(pady=10)

    label_nombre = ttk.Label(frame_barra_texto, text="Nombre:")
    label_nombre.pack(side=tk.LEFT)

    entry_nombre = ttk.Entry(frame_barra_texto, width=50)
    entry_nombre.pack(side=tk.LEFT)

    frame_barra_texto = ttk.Frame(frame_principal)
    frame_barra_texto.pack(pady=10)

    label_autor = ttk.Label(frame_barra_texto, text="Autor:")
    label_autor.pack(side=tk.LEFT)

    entry_autor = ttk.Entry(frame_barra_texto, width=50)
    entry_autor.pack(side=tk.LEFT)

    frame_barra_texto = ttk.Frame(frame_principal)
    frame_barra_texto.pack(pady=10)

    label_anio = ttk.Label(frame_barra_texto, text="Año:")
    label_anio.pack(side=tk.LEFT)

    entry_anio = ttk.Entry(frame_barra_texto, width=50)
    entry_anio.pack(side=tk.LEFT)

    frame_barra_texto = ttk.Frame(frame_principal)
    frame_barra_texto.pack(pady=10)

    label_genero = ttk.Label(frame_barra_texto, text="Género:")
    label_genero.pack(side=tk.LEFT)

    entry_genero = ttk.Entry(frame_barra_texto, width=50)
    entry_genero.pack(side=tk.LEFT)

    frame_barra_texto = ttk.Frame(frame_principal)
    frame_barra_texto.pack(pady=10)

    label_cantidad = ttk.Label(frame_barra_texto, text="Cantidad:")
    label_cantidad.pack(side=tk.LEFT)

    entry_cantidad = ttk.Entry(frame_barra_texto, width=50)
    entry_cantidad.pack(side=tk.LEFT)

    frame_barra_texto = ttk.Frame(frame_principal)
    frame_barra_texto.pack(pady=10)

    label_buscar = ttk.Label(frame_barra_texto, text="Buscar:")
    label_buscar.pack(side=tk.LEFT)

    entry_buscar_libro_admin = ttk.Entry(frame_barra_texto, width=50)
    entry_buscar_libro_admin.pack(side=tk.LEFT)
    entry_buscar_libro_admin.bind('<Return>', lambda event: buscar_libro())

    # Botones de administración
    frame_botones_admin = ttk.Frame(ventana_admin)
    frame_botones_admin.pack(pady=10)

    boton_agregar_libro = ttk.Button(frame_botones_admin, text="Agregar libro", command=agregar_libro)
    boton_agregar_libro.pack(side=tk.LEFT, padx=5)

    boton_agregar_libro = ttk.Button(frame_botones_admin, text="Revisar", command=revisar)
    boton_agregar_libro.pack(side=tk.LEFT, padx=5)

    boton_editar_libro = ttk.Button(frame_botones_admin, text="Editar libro", command=editar_libro)
    boton_editar_libro.pack(side=tk.LEFT, padx=5)

    boton_eliminar_libro = ttk.Button(frame_botones_admin, text="Eliminar libro", command=eliminar_libro)
    boton_eliminar_libro.pack(side=tk.LEFT, padx=5)

    boton_ver_libros = ttk.Button(frame_botones_admin, text="Ver todos los libros", command=ver_libros)
    boton_ver_libros.pack(side=tk.LEFT, padx=5)

    boton_administrar_clientes = ttk.Button(frame_botones_admin, text="Administrar clientes", command=abrir_ventana_admin_clientes)
    boton_administrar_clientes.pack(side=tk.LEFT, padx=5)

    boton_ver_libros = ttk.Button(frame_botones_admin, text="Guardar", command=guardar_datos)
    boton_ver_libros.pack(side=tk.LEFT, padx=5)

    treeview_libros.pack(fill=tk.BOTH, expand=True)

    # Botones de categorías
    frame_categorias = ttk.Frame(ventana_admin)
    frame_categorias.pack(pady=10)

    boton_ciencia_ficcion = ttk.Button(frame_categorias, text="Ciencia Ficción", width=15, command=ciencia_ficcion)
    boton_ciencia_ficcion.grid(row=0, column=0, padx=5, pady=5)


    boton_fantasia = ttk.Button(frame_categorias, text="Fantasía", width=10, command=fantasia)
    boton_fantasia.grid(row=0, column=1, padx=5, pady=5)

    boton_romance = ttk.Button(frame_categorias, text="Romance", width=10, command=romance)
    boton_romance.grid(row=0, column=2, padx=5, pady=5)

    boton_poesia = ttk.Button(frame_categorias, text="Poesía", width=10, command=poesia)
    boton_poesia.grid(row=0, column=3, padx=5, pady=5)

    boton_ficcion = ttk.Button(frame_categorias, text="Ficción", width=10, command=ficcion)
    boton_ficcion.grid(row=0, column=4, padx=5, pady=5)

    ventana_admin.mainloop()




##############################################################################################################################################




def abrir_ventana_admin_clientes():
    ventana_admin_cliente = tk.Toplevel(ventana_principal)
    ventana_admin_cliente.title("Admin")
    ventana_admin_cliente.geometry("800x600")

    # Establecer estilo
    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 14, "bold"))
    style.configure("TButton", font=("Arial", 12), padding=10)

    # Treeview de clientes
    treeview_clientes = ttk.Treeview(ventana_admin_cliente, column=('Nombre','ID','Direccion','Telefono'))
    treeview_clientes.heading('#0', text='Nombre')
    treeview_clientes.heading('#1', text='ID')
    treeview_clientes.heading('#2', text='Dirección')
    treeview_clientes.heading('#3', text='Teléfono')    

    def agregar_cliente():
        nombre = entry_nombre.get()
        id = entry_id.get()
        direccion = entry_direccion.get()
        telefono = entry_telefono.get()
        
        if nombre != '' and id != '' and direccion != '' and telefono != '':
            clientes.add(nombre, int(id), direccion, telefono)
            treeview_clientes.insert('', 'end', text=nombre, values=(id, direccion, telefono))
        
        entry_nombre.delete(0, 'end')
        entry_id.delete(0, 'end')
        entry_direccion.delete(0, 'end')
        entry_telefono.delete(0, 'end')

    def editar_cliente():
        try:
            entry_nombre.delete(0, 'end')
            entry_id.delete(0, 'end')
            entry_direccion.delete(0, 'end')
            entry_telefono.delete(0, 'end')
            
            nombre = treeview_clientes.item(treeview_clientes.selection())['text']
            id = int(treeview_clientes.item(treeview_clientes.selection())['values'][0])
            direccion = treeview_clientes.item(treeview_clientes.selection())['values'][1]
            telefono = treeview_clientes.item(treeview_clientes.selection())['values'][2]
            
            entry_nombre.insert(0, nombre)
            entry_id.insert(0, id)
            entry_direccion.insert(0, direccion)
            entry_telefono.insert(0, telefono)
            
        except:
            pass

    def eliminar_cliente():
        id_actual = int(treeview_clientes.item(treeview_clientes.selection())['values'][0])
        clientes.remove(id_actual)
        treeview_clientes.delete(treeview_clientes.selection())

    def clear():
        for item in treeview_clientes.get_children():
            treeview_clientes.delete(item)

    def ver_clientes():
        ct = 0
        clear()
        if ct == 20:
            return
        else:
            for i in clientes.arr:
                if i == None:
                    continue
                actual = i.head
                while actual:
                    treeview_clientes.insert('', 'end', text=actual.key.nombre, values=(actual.key.id, actual.key.direccion, actual.key.telefono))
                    actual = actual.next
                    ct += 1


    def guardar_clientes():
        nombre = entry_nombre.get()
        id = int(entry_id.get())
        direccion = entry_direccion.get()
        telefono = entry_telefono.get()
        
        if nombre != '' and id != '' and direccion != '' and telefono != '':
            id_actual = int(treeview_clientes.item(treeview_clientes.selection())['values'][0])
            clientes.remove(id_actual)
            clientes.add(nombre, id, direccion, telefono)
            
            treeview_clientes.item(treeview_clientes.selection(), text=nombre)
            treeview_clientes.item(treeview_clientes.selection(), values=(id, direccion, telefono))
            
            entry_nombre.delete(0, 'end')
            entry_id.delete(0, 'end')
            entry_direccion.delete(0, 'end')
            entry_telefono.delete(0, 'end')

    def buscar_cliente():        
        id = entry_buscar_cliente_admin.get()
        try:
            id = int(id)
            if clientes.find(id):
                clear()
                treeview_clientes.insert('', 'end', text=clientes.find(id).nombre, values=(clientes.find(id).id, clientes.find(id).direccion, clientes.find(id).telefono))
                entry_buscar_cliente_admin.delete(0, 'end')
            else:
                pass
        except:
            pass

    def revisar():
        clientes.remove(5678913)
        clientes.printTable()

    # Frame principal
    frame_principal = ttk.Frame(ventana_admin_cliente)
    frame_principal.pack(pady=10)

    # Barra de texto y etiquetas
    frame_barra_texto = ttk.Frame(frame_principal)
    frame_barra_texto.pack(pady=10)

    label_nombre = ttk.Label(frame_barra_texto, text="Nombre:")
    label_nombre.pack(side=tk.LEFT)

    entry_nombre = ttk.Entry(frame_barra_texto, width=50)
    entry_nombre.pack(side=tk.LEFT)

    frame_barra_texto = ttk.Frame(frame_principal)
    frame_barra_texto.pack(pady=10)

    label_id = ttk.Label(frame_barra_texto, text="Id:")
    label_id.pack(side=tk.LEFT)

    entry_id = ttk.Entry(frame_barra_texto, width=50)
    entry_id.pack(side=tk.LEFT)

    frame_barra_texto = ttk.Frame(frame_principal)
    frame_barra_texto.pack(pady=10)

    label_direccion = ttk.Label(frame_barra_texto, text="Dirección:")
    label_direccion.pack(side=tk.LEFT)

    entry_direccion = ttk.Entry(frame_barra_texto, width=50)
    entry_direccion.pack(side=tk.LEFT)

    frame_barra_texto = ttk.Frame(frame_principal)
    frame_barra_texto.pack(pady=10)

    label_telefono = ttk.Label(frame_barra_texto, text="Teléfono:")
    label_telefono.pack(side=tk.LEFT)

    entry_telefono = ttk.Entry(frame_barra_texto, width=50)
    entry_telefono.pack(side=tk.LEFT)

    frame_barra_texto = ttk.Frame(frame_principal)
    frame_barra_texto.pack(pady=10)

    label_buscar_cliente_admin = ttk.Label(frame_barra_texto, text="Buscar:")
    label_buscar_cliente_admin.pack(side=tk.LEFT)

    entry_buscar_cliente_admin = ttk.Entry(frame_barra_texto, width=50)
    entry_buscar_cliente_admin.pack(side=tk.LEFT)
    entry_buscar_cliente_admin.bind('<Return>', lambda event: buscar_cliente())

    # Botones de administración
    frame_botones_admin = ttk.Frame(ventana_admin_cliente)
    frame_botones_admin.pack(pady=10)

    boton_agregar_libro = ttk.Button(frame_botones_admin, text="Agregar cliente", command=agregar_cliente)
    boton_agregar_libro.pack(side=tk.LEFT, padx=5)

    boton_editar_libro = ttk.Button(frame_botones_admin, text="Editar cliente", command=editar_cliente)
    boton_editar_libro.pack(side=tk.LEFT, padx=5)

    boton_eliminar_libro = ttk.Button(frame_botones_admin, text="Eliminar cliente", command=eliminar_cliente)
    boton_eliminar_libro.pack(side=tk.LEFT, padx=5)

    boton_ver_libros = ttk.Button(frame_botones_admin, text="Ver todos los clientes", command=ver_clientes)
    boton_ver_libros.pack(side=tk.LEFT, padx=5)

    boton_guardar_cliente = ttk.Button(frame_botones_admin, text="Guardar", command=guardar_clientes)
    boton_guardar_cliente.pack(side=tk.LEFT, padx=5)

    boton_guardar_cliente = ttk.Button(frame_botones_admin, text="Revisar", command=revisar)
    boton_guardar_cliente.pack(side=tk.LEFT, padx=5)

    treeview_clientes.pack(fill=tk.BOTH, expand=True)
    ver_clientes()

    ventana_admin_cliente.mainloop()




##############################################################################################################################################




def abrir_ventana_clientes():
    global treeview_libros
    ventana_clientes = tk.Toplevel(ventana_principal)
    ventana_clientes.title("Clientes")
    ventana_clientes.geometry("1000x600")

    # Treeview de libros
    treeview_libros = ttk.Treeview(ventana_clientes, column=('Nombre','Autor','Año','Genero','Cantidad'))
    treeview_libros.heading('#0', text='Nombre')
    treeview_libros.heading('#1', text='Autor')
    treeview_libros.heading('#2', text='Año')
    treeview_libros.heading('#3', text='Genero')
    treeview_libros.heading('#4', text='Cantidad')

    def clear():
        for item in treeview_libros.get_children():
            treeview_libros.delete(item)

    def ver_libros():
        ct = 0
        clear()
        if ct == 20:
            return
        else:
            for i in libros.arr:
                if i == None:
                    continue
                actual = i.head
                while actual:
                    treeview_libros.insert('', 'end', text=actual.key.nombre, values=(actual.key.autor, actual.key.year, actual.key.genero, actual.key.cantidad))
                    actual = actual.next
                    ct += 1

    ver_libros()

    def ciencia_ficcion():
        clear()
        actual = categorias.cienciaFiccion.head
        while actual:                        
            treeview_libros.insert('', 'end', text=libros.find(actual.key).nombre, values=(libros.find(actual.key).nombre, libros.find(actual.key).year, libros.find(actual.key).genero, libros.find(actual.key).cantidad))
            actual = actual.next

    def fantasia():
        clear()
        actual = categorias.fantasia.head
        while actual:                        
            treeview_libros.insert('', 'end', text=libros.find(actual.key).nombre, values=(libros.find(actual.key).nombre, libros.find(actual.key).year, libros.find(actual.key).genero, libros.find(actual.key).cantidad))
            actual = actual.next

    def romance():
        clear()
        actual = categorias.romance.head
        while actual:                        
            treeview_libros.insert('', 'end', text=libros.find(actual.key).nombre, values=(libros.find(actual.key).nombre, libros.find(actual.key).year, libros.find(actual.key).genero, libros.find(actual.key).cantidad))
            actual = actual.next

    def poesia():
        clear()
        actual = categorias.poesia.head
        while actual:                        
            treeview_libros.insert('', 'end', text=libros.find(actual.key).nombre, values=(libros.find(actual.key).nombre, libros.find(actual.key).year, libros.find(actual.key).genero, libros.find(actual.key).cantidad))
            actual = actual.next

    def ficcion():
        clear()
        actual = categorias.ficcion.head
        while actual:                        
            treeview_libros.insert('', 'end', text=libros.find(actual.key).nombre, values=(libros.find(actual.key).nombre, libros.find(actual.key).year, libros.find(actual.key).genero, libros.find(actual.key).cantidad))
            actual = actual.next

    def buscar_libro():        
        nombre = entry_buscar_libro_cliente.get()
        if libros.find(nombre):
            clear()
            treeview_libros.insert('', 'end', text=libros.find(nombre).nombre, values=(libros.find(nombre).nombre, libros.find(nombre).year, libros.find(nombre).genero, libros.find(nombre).cantidad))
            entry_buscar_libro_cliente.delete(0, 'end')
        else:
            pass

    def revisar():
        libros.printTable()

    # Etiqueta "Buscar"
    frame_buscar = ttk.Frame(ventana_clientes)
    frame_buscar.pack(pady=10)

    label_buscar = ttk.Label(frame_buscar, text="Buscar:")
    label_buscar.pack(side=tk.LEFT)

    # Barra de búsqueda
    entry_buscar_libro_cliente = ttk.Entry(frame_buscar, width=50)
    entry_buscar_libro_cliente.pack(side=tk.LEFT)
    entry_buscar_libro_cliente.bind('<Return>', lambda event: buscar_libro())

    # Botones de categorías
    frame_categorias = ttk.Frame(ventana_clientes)
    frame_categorias.pack(pady=10)

    boton_ciencia_ficcion = ttk.Button(frame_categorias, text="Ciencia Ficción", width=15, command=ciencia_ficcion)
    boton_ciencia_ficcion.pack(side=tk.LEFT, padx=5)

    boton_fantasia = ttk.Button(frame_categorias, text="Fantasía", width=15, command=fantasia)
    boton_fantasia.pack(side=tk.LEFT, padx=5)

    boton_romance = ttk.Button(frame_categorias, text="Romance", width=15, command=romance)
    boton_romance.pack(side=tk.LEFT, padx=5)

    boton_poesia = ttk.Button(frame_categorias, text="Poesía", width=15, command=poesia)
    boton_poesia.pack(side=tk.LEFT, padx=5)

    boton_ficcion = ttk.Button(frame_categorias, text="Ficción", width=15, command=ficcion)
    boton_ficcion.pack(side=tk.LEFT, padx=5)

    boton_ficcion = ttk.Button(frame_categorias, text="Revisar", width=15, command=revisar)
    boton_ficcion.pack(side=tk.LEFT, padx=5)

    # Treeview
    treeview_libros.pack(fill=tk.BOTH, expand=True)

    # Botones "Mostrar Todos", "Comprar" y "Ver estado de pedidos"
    frame_botones = ttk.Frame(ventana_clientes)
    frame_botones.pack(pady=10)

    boton_mostrar_todos = ttk.Button(frame_botones, text="Mostrar Todos los Libros", width=20, command=ver_libros)
    boton_mostrar_todos.pack(side=tk.LEFT, padx=5)

    boton_comprar = ttk.Button(frame_botones, text="Comprar", width=10, command=abrir_ventana_compra)
    boton_comprar.pack(side=tk.LEFT, padx=5)
    
    boton_ver_pedidos = ttk.Button(frame_botones, text="Ver Estado de Pedidos", width=20)
    boton_ver_pedidos.pack(side=tk.LEFT, padx=5)
    boton_ver_pedidos.configure(command=abrir_ventana_historial_pedidos)





##############################################################################################################################################




def abrir_ventana_historial_pedidos():
    ventana_historial = tk.Toplevel(ventana_principal)
    ventana_historial.title("Historial de Pedidos")
    ventana_historial.geometry("800x600")

    # Treeview de pedidos
    treeview_pedidos = ttk.Treeview(ventana_historial, column=('Nombre de libro','Id cliente','Destino','Estado','Tiempo'))
    treeview_pedidos.heading('#0', text='Nombre de libro')
    treeview_pedidos.heading('#1', text='Id cliente')
    treeview_pedidos.heading('#2', text='Destino')
    treeview_pedidos.heading('#3', text='Estado')
    treeview_pedidos.heading('#4', text='Tiempo')

    def clear():
        for item in treeview_pedidos.get_children():
            treeview_pedidos.delete(item)

    def ver_pedidos():
        id_cliente = entry_id_cliente.get()
        if id_cliente != '':
            id_cliente = int(id_cliente)
            ct = 0
            clear()
            if ct == 20:
                return
            else:
                for pedido in clientes.find(id_cliente).pedidos:
                    treeview_pedidos.insert('', 'end', text=pedido.libro.nombre, values=(pedido.cliente.id, pedido.destino, pedido.estado, pedido.tiempo))
                    ct += 1

    # Texto en forma de título
    titulo = ttk.Label(ventana_historial, text="Historial de Pedidos", font=("Arial", 16, "bold"))
    titulo.pack(pady=20)

    frame_principal = ttk.Frame(ventana_historial)
    frame_principal.pack(pady=10)

    frame_barra_texto = ttk.Frame(frame_principal)
    frame_barra_texto.pack(pady=10)

    label_id_cliente = ttk.Label(frame_barra_texto, text="Id:")
    label_id_cliente.pack(side=tk.LEFT)

    entry_id_cliente = ttk.Entry(frame_barra_texto, width=50)
    entry_id_cliente.pack(side=tk.LEFT)
    entry_id_cliente.bind('<Return>', lambda event: ver_pedidos())

    treeview_pedidos.pack(fill=tk.BOTH, expand=True)

    ventana_historial.mainloop()




##############################################################################################################################################




def abrir_ventana_compra():
    if treeview_libros.selection():
        try:
            nombre_actual = treeview_libros.item(treeview_libros.selection())['text']
            cantidad = treeview_libros.item(treeview_libros.selection())['values'][3]
            # Crear la ventana secundaria
            ventana_compra = tk.Toplevel(ventana_principal)
            ventana_compra.title("Realizar compra")

            def completar_compra():
                id_cliente = entry_id_cliente.get()
                if id_cliente != '':
                    id_cliente = int(id_cliente)
                    if clientes.find(id_cliente):
                        destino = clientes.find(id_cliente).direccion
                        if cantidad >= 1:
                            libros.find(nombre_actual).cantidad = libros.find(nombre_actual).cantidad - 1 
                            pedido = Pedido(nombre_actual, id_cliente, destino, "Entregado")
                            clientes.find(id_cliente).pedidos.append(pedido)
                            messagebox.showwarning("Advertencia", "El pedido llegara en " + str(pedido.tiempo) + " minutos.")
                        else:
                            pedido = Pedido(nombre_actual, id_cliente, destino, "Pendiente")
                            clientes.find(id_cliente).pedidos.append(pedido)
                            messagebox.showwarning("Advertencia", "El libro no se encuentra disponible, has sido añadido a la fila.")
                            libros.find(nombre_actual).fila.insert(pedido)

            # Estilos
            estilo_etiquetas = ttk.Style()
            estilo_etiquetas.configure('EstiloEtiquetas.TLabel', font=('Arial', 12))

            estilo_entrys = ttk.Style()
            estilo_entrys.configure('EstiloEntrys.TEntry', font=('Arial', 12))

            estilo_boton = ttk.Style()
            estilo_boton.configure('EstiloBoton.TButton', font=('Arial', 12))

            # Etiqueta de título
            etiqueta_titulo = ttk.Label(ventana_compra, text="Realizar compra", style='EstiloEtiquetas.TLabel')
            etiqueta_titulo.grid(row=0, column=0, columnspan=2, pady=10)

            # Entry para el ID del cliente
            etiqueta_id_cliente = ttk.Label(ventana_compra, text="ID del cliente:", style='EstiloEtiquetas.TLabel')
            etiqueta_id_cliente.grid(row=2, column=0, padx=10, pady=5)
            entry_id_cliente = ttk.Entry(ventana_compra, style='EstiloEntrys.TEntry')
            entry_id_cliente.grid(row=2, column=1, padx=10, pady=5)

            # Botón "Completar"
            boton_completar = ttk.Button(ventana_compra, text="Completar", style='EstiloBoton.TButton', command=completar_compra)
            boton_completar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        except:
            pass



##############################################################################################################################################




# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Ventana de Selección")
ventana_principal.geometry("400x400")
ventana_principal.configure(bg="#3A5F42")

# Establecer estilo
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=10)
style.configure("TLabel", font=("Arial", 14, "bold"))

# Crear el título
label_titulo = ttk.Label(ventana_principal, text="Seleccione una opción", background="#3A5F42", foreground="#F7F3E9" )
label_titulo.pack(pady=20)

# Crear los botones
boton_admin = ttk.Button(ventana_principal, text="Admin", command=abrir_ventana_admin)
boton_admin.pack(pady=10)
boton_cliente = ttk.Button(ventana_principal, text="Cliente", command=abrir_ventana_clientes)
boton_cliente.pack(pady=10)

# Iniciar el bucle principal de la ventana
ventana_principal.mainloop()

