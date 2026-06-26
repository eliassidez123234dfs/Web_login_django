from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from products.models import Producto


class Command(BaseCommand):
    help = 'Crea datos de prueba: usuarios y productos'

    def handle(self, *args, **options):
        self.stdout.write('Creando datos de prueba...\n')

        # --- Usuarios de prueba ---
        usuarios_data = [
            {'username': 'admin', 'password': 'admin123', 'is_staff': True, 'is_superuser': True},
            {'username': 'usuario1', 'password': 'test1234'},
            {'username': 'usuario2', 'password': 'test1234'},
            {'username': 'usuario3', 'password': 'test1234'},
            {'username': 'usuario4', 'password': 'test1234'},
            {'username': 'usuario5', 'password': 'test1234'},
            {'username': 'usuario6', 'password': 'test1234'},
            {'username': 'usuario7', 'password': 'test1234'},
            {'username': 'usuario8', 'password': 'test1234'},
            {'username': 'usuario9', 'password': 'test1234'},
            {'username': 'usuario10', 'password': 'test1234'},
        ]

        creados = 0
        for data in usuarios_data:
            username = data['username']
            if User.objects.filter(username=username).exists():
                self.stdout.write(f'  Usuario {username} ya existe, omitiendo.\n')
                continue
            user = User.objects.create_user(
                username=username,
                password=data['password'],
                email=f'{username}@red.test',
            )
            if data.get('is_staff'):
                user.is_staff = True
                user.is_superuser = True
                user.save()
            creados += 1
            self.stdout.write(f'  Usuario creado: {username} / {data["password"]}\n')

        self.stdout.write(f'\n{creados} usuario(s) creado(s).\n')

        # --- Productos de prueba ---
        productos_data = [
            {'nombre': 'Camiseta Clásica Negra', 'precio': 45000, 'descripcion': 'Camiseta de algodón peinado 180g. Corte recto, cuello redondo. Ideal para estampación serigráfica.'},
            {'nombre': 'Hoodie Premium Gris', 'precio': 95000, 'descripcion': 'Hoodie en algodón fleece 300g. Bolsillo tipo canguro, capucha forrada, ajuste moderno.'},
            {'nombre': 'Tote Bag Crudo', 'precio': 22000, 'descripcion': 'Bolsa de tela en algodón crudo 140g. Asas largas, capacidad para 10 kg.'},
            {'nombre': 'Gorra Trucker Roja', 'precio': 32000, 'descripcion': 'Gorra trucker con frente de algodón y malla trasera. Cierre ajustable.'},
            {'nombre': 'Camiseta Estampada "RUIDO"', 'precio': 55000, 'descripcion': 'Camiseta oversize con estampado frontal. Algodón 200g, costuras reforzadas.'},
            {'nombre': 'Camiseta Estampada "SELVA"', 'precio': 55000, 'descripcion': 'Diseño de fauna tropical estampado en serigrafía. Algodón orgánico.'},
            {'nombre': 'Camiseta Estampada "OLEAJE"', 'precio': 55000, 'descripcion': 'Estampado olas en degradado. Fit regular, manga corta.'},
            {'nombre': 'Camiseta Estampada "FUEGO"', 'precio': 55000, 'descripcion': 'Diseño abstracto llama. Serigrafía a 4 tintas. Algodón premium.'},
            {'nombre': 'Camiseta Estampada "URBANO"', 'precio': 50000, 'descripcion': 'Estilo grafiti urbano. Tinta fluorescente. Corte slim fit.'},
            {'nombre': 'Camiseta Estampada "RETRO"', 'precio': 52000, 'descripcion': 'Estampado vintage años 90. Algodón 180g, acabado lavado.'},
            {'nombre': 'Tote Bag Estampada "ARCHIVO"', 'precio': 28000, 'descripcion': 'Tote bag con estampado tipográfico. Algodón crudo 160g.'},
            {'nombre': 'Hoodie Estampado "SOMBRA"', 'precio': 105000, 'descripcion': 'Hoodie con estampado espalda completa. Algodón fleece 320g.'},
        ]

        creados_p = 0
        for data in productos_data:
            if Producto.objects.filter(nombre=data['nombre']).exists():
                self.stdout.write(f'  Producto "{data["nombre"]}" ya existe, omitiendo.\n')
                continue
            Producto.objects.create(
                nombre=data['nombre'],
                precio=data['precio'],
                descripcion=data['descripcion'],
                disponible=True,
            )
            creados_p += 1
            self.stdout.write(f'  Producto creado: {data["nombre"]} — ${data["precio"]:,}\n')

        self.stdout.write(f'\n{creados_p} producto(s) creado(s).\n')
        self.stdout.write(self.style.SUCCESS('\n¡Datos de prueba creados exitosamente!'))
