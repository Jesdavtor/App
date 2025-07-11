# Checklist de mejoras para el proyecto Django

## Seguridad y buenas prácticas
- [x] Desactivar DEBUG en producción (`DEBUG=False`)
- [ ] Configurar correctamente `ALLOWED_HOSTS`
- [ ] Usar archivo `.env` local para variables sensibles

## Mejorar la API
- [ ] Agregar autenticación (Token o JWT)
- [ ] Implementar paginación y filtros en endpoints
- [ ] Documentar la API (Swagger o DRF-YASG)

## Mejorar el frontend
- [ ] Crear plantillas personalizadas para vistas
- [ ] Integrar Bootstrap u otro framework CSS
- [ ] Agregar validaciones y mensajes de éxito/error en formularios

## Automatización y pruebas
- [ ] Agregar pruebas unitarias y de integración
- [ ] Configurar CI/CD (por ejemplo, GitHub Actions)

## Internacionalización y localización
- [ ] Configurar traducciones (i18n)
- [ ] Ajustar `LANGUAGE_CODE` y `TIME_ZONE`

## Optimización y monitoreo
- [ ] Activar compresión de archivos estáticos (WhiteNoise ya lo permite)
- [ ] Configurar logging para monitoreo de errores
- [ ] Integrar herramientas de monitoreo (Sentry, Datadog, etc.)

## Personalización del admin
- [ ] Personalizar header, título y colores del admin
- [ ] Agregar filtros, búsquedas y acciones personalizadas 