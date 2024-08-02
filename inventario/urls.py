from django.urls import path
from . import views

app_name = "inventario"

urlpatterns = [
path('login', views.Login.as_view(), name='login'),
path('panel', views.Panel.as_view(), name='panel'),
path('salir', views.Salir.as_view(), name='salir'),
path('perfil/<str:modo>/<int:p>', views.Perfil.as_view(), name='perfil'),
path('eliminar/<str:modo>/<int:p>', views.Eliminar.as_view(), name='eliminar'),

path('listarCategorias', views.ListarCategorias.as_view(), name='listarCategorias'),
path('agregarCategoria', views.AgregarCategoria.as_view(), name='agregarCategoria'),
path('importarCategorias', views.ImportarCategorias.as_view(), name='importarCategorias'),
path('exportarCategorias', views.ExportarCategorias.as_view(), name='exportarCategorias'),
path('editarCategoria/<int:p>', views.EditarCategoria.as_view(), name='editarCategoria'),

path('listarProductos', views.ListarProductos.as_view(), name='listarProductos'),
path('agregarProducto', views.AgregarProducto.as_view(), name='agregarProducto'),
path('importarProductos', views.ImportarProductos.as_view(), name='importarProductos'),
path('exportarProductos', views.ExportarProductos.as_view(), name='exportarProductos'),
path('editarProducto/<int:p>', views.EditarProducto.as_view(), name='editarProducto'),

path('listarProveedores', views.ListarProveedores.as_view(), name='listarProveedores'),
path('agregarProveedor', views.AgregarProveedor.as_view(), name='agregarProveedor'),
path('importarProveedores', views.ImportarProveedores.as_view(), name='importarProveedores'),
path('exportarProveedores', views.ExportarProveedores.as_view(), name='exportarProveedores'),
path('editarProveedor/<int:p>', views.EditarProveedor.as_view(), name='editarProveedor'),

path('agregarPedido', views.AgregarPedido.as_view(), name='agregarPedido'),
path('listarPedidos', views.ListarPedidos.as_view(), name='listarPedidos'),
path('detallesPedido', views.DetallesPedido.as_view(), name='detallesPedido'),
path('verPedido/<int:p>',views.VerPedido.as_view(), name='verPedido'),
path('validarPedido/<int:p>',views.ValidarPedido.as_view(), name='validarPedido'),
path('generarPedido/<int:p>',views.GenerarPedido.as_view(), name='generarPedido'),
path('generarPedidoPDF/<int:p>',views.GenerarPedidoPDF.as_view(), name='generarPedidoPDF'),

path('listarClientes', views.ListarClientes.as_view(), name='listarClientes'),
path('agregarCliente', views.AgregarCliente.as_view(), name='agregarCliente'),
path('importarClientes', views.ImportarClientes.as_view(), name='importarClientes'),
path('exportarClientes', views.ExportarClientes.as_view(), name='exportarClientes'),
path('editarCliente/<int:p>', views.EditarCliente.as_view(), name='editarCliente'),

path('emitirFactura', views.EmitirFactura.as_view(), name='emitirFactura'),
path('detallesDeFactura', views.DetallesFactura.as_view(), name='detallesDeFactura'),
path('listarFacturas',views.ListarFacturas.as_view(), name='listarFacturas'),
path('verFactura/<int:p>',views.VerFactura.as_view(), name='verFactura'),
path('generarFactura/<int:p>',views.GenerarFactura.as_view(), name='generarFactura'),
path('generarFacturaPDF/<int:p>',views.GenerarFacturaPDF.as_view(), name='generarFacturaPDF'),

path('crearUsuario',views.CrearUsuario.as_view(), name='crearUsuario'),
path('listarUsuarios', views.ListarUsuarios.as_view(), name='listarUsuarios'),

path('importarBDD',views.ImportarBDD.as_view(), name='importarBDD'),
path('descargarBDD', views.DescargarBDD.as_view(), name='descargarBDD'),
path('configuracionGeneral', views.ConfiguracionGeneral.as_view(), name='configuracionGeneral'),

path('verManualDeUsuario/<str:pagina>/',views.VerManualDeUsuario.as_view(), name='verManualDeUsuario'),

#rutas para el manejo del Kardex
# path('kardex/lista_productos/', ListaProductosView.as_view(), name='lista_productos'),
# path('kardex/detalle_kardex/<int:producto_id>/', DetalleKardexView.as_view(), name='detalle_kardex'),
# path('kardex/resumen_kardex/<int:producto_id>/', ResumenKardexView.as_view(), name='resumen_kardex'),
# path('kardex/nuevo_movimiento/<int:producto_id>/', NuevoMovimientoView.as_view(), name='nuevo_movimiento'),
# path('kardex/registrar_movimiento/<int:producto_id>/', RegistrarMovimientoView.as_view(), name='registrar_movimiento'),
path('lista_productos/', views.ListaProductosView.as_view(), name='lista_productos'),
path('detalle_kardex/<int:producto_id>/', views.DetalleKardexView.as_view(), name='detalle_kardex'),
path('resumen_kardex/<int:producto_id>/', views.ResumenKardexView.as_view(), name='resumen_kardex'),
path('nuevo_movimiento/<int:producto_id>/', views.NuevoMovimientoView.as_view(), name='nuevo_movimiento'),
path('registrar_movimiento/<int:producto_id>/', views.RegistrarMovimientoView.as_view(), name='registrar_movimiento'),

]

