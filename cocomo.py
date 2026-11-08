import numpy as np
from matplotlib import pyplot as plt
import colorama as colorama
from colorama import Fore

def formula():
    global sumatoria_xy, sumatoria_x_cuadrada
    sumatoria_xy = np.sum(x * y)
    sumatoria_x_cuadrada = np.sum(x ** 2)
    m = sumatoria_xy / sumatoria_x_cuadrada
    return m

def comprobar_derivada():
    m = formula()
    ds_dm = (sumatoria_xy) - (m * sumatoria_x_cuadrada)
    return ds_dm

def comprobar_segunda_derivada():
    d2s_dm2 = 2 * np.sum(x**2)
    return d2s_dm2

def evalucacion_error():
    m = formula()
    y_predict = m * x
    residuos = y - y_predict
    error_total_acumulado = np.sum(residuos ** 2)
    return error_total_acumulado

def pendiente(xs, ys):
    return np.sum(xs * ys) / np.sum(xs ** 2)


def results():
    m = formula()
    verficacion = False
    verficacion2 = False
    verificacionMessage = ""
    verificacionMessage = ""

    if comprobar_derivada() == 0.0:
        verficacion = True
        verificacionMessage = Fore.GREEN + "Comprobado." + Fore.WHITE
    else: verificacionMessage = Fore.RED + "No comprobado." + Fore.WHITE

    if comprobar_segunda_derivada() > 0.0:
        verficacion2 = True
        verificacionMessage2 = Fore.GREEN + "Comprobado, es un minimo absoluto." + Fore.WHITE
    else: verificacionMessage2 = Fore.RED + "No comprobado, no es un minimo absoluto." + Fore.WHITE
        

    print(f"""
    {Fore.WHITE}
    ------- Resumen -------
    {Fore.BLUE}
    Datos
    x = {x}
    y = {y}
    {Fore.YELLOW}
    Sumatorias
    Sumatoria de x * y = {sumatoria_xy}
    Sumatoria de x cuadrada = {sumatoria_x_cuadrada}
    {Fore.GREEN}
    Resultado de aplicación de formula:
    Pendiente [m] = {m:.3f} Horas/kloc aprox
    {Fore.CYAN}
    Comprobación:
    derivada original = Σ(xi_y_i -mx_i**2) = 0
    resultado reemplazando resultados obtenidos: {comprobar_derivada()}
    ¿El resultado es 0?
    {verficacion}
    {verificacionMessage}
    segunda derivada original = 2Σ(x**2_i)
    resultado reemplazando resultados obtenidos: {comprobar_segunda_derivada()}
    ¿El resultado es mayor que 0?
    {verficacion2}
    {verificacionMessage2}
    {Fore.MAGENTA}
    Errores cuadraticos: {evalucacion_error():.2f}
    {Fore.RED}
    Sensibilidad ante proyectos atípicos:
    Pendiente original con 10 proyectos (m*): {m:.3f}
    Pendiente sin el proyecto 10 (m*_mod): {m_sin_outlier:.3f}
    Cambio: {cambio:.2f} %
    {Fore.WHITE}
    """)

x = np.array([6, 8, 11, 13, 18, 21, 27, 32, 40, 50])
y = np.array([144, 224, 304, 336, 520, 592, 816, 1008, 1280, 1680])
m = formula()
x_linea = np.linspace(0, max(x) + 5)
y_linea = m * x_linea
x_sin_outlier = x[:-1]
y_sin_outlier = y[:-1]
m_sin_outlier = pendiente(x_sin_outlier, y_sin_outlier)
cambio = (m_sin_outlier - m) / m * 100
error = np.sqrt(evalucacion_error() / (len(x) - 1))
results()

plt.scatter(x, y, color = "black", label = "Datos")
plt.plot(x_linea, y_linea, color = 'blue', linewidth = 2, label="Ajuste")
plt.errorbar(x, y, yerr = error, fmt = 'o', color = "black", capsize = 4, label = "Barras de error")
plt.plot(x_linea, y_linea, color = 'blue', linewidth = 2, label = f"Ajuste: $\\hat{{y}} = {m:.1f}\\,x$")
plt.title("Calibración del Modelo COCOMO")
plt.xlabel("KLOC")
plt.ylabel("Horas-Hombre")
plt.legend()
plt.show()