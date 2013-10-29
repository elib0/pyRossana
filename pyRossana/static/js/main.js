/**
 * Muestra cuadro de dialogo por Jquery ui
 * @param  {String}  content Contenido de la ventana principal
 * @param  {Boolean} isModal Si el cuadro de dialogo es modal
 * @param  {Object}  btns    Objeto con botones y sus respectivas acciones
 * @param  {String}  tit     Titulos de la ventana
 * @return {none}          none
 */
function showDialog(content, isModal, btns, tit){
if(!btns){
	btns = [{
		text: "Aceptar",
		click: function() {
			$( this ).dialog( "close" );
		}
	}]; 
}
$('#dialog').attr('title', tit || 'Info').html(content).dialog({
	modal: isModal || true,
	show: {
		effect: "slide",
		duration: 400
	},
	buttons: btns
});
}