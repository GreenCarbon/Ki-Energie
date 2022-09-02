
// var a = "{{ddl_sel_kunde}}";
// var b = "{{dsp_eckdaten}}";

// alert(a & ' ' & b)

function checkChange(control) {
    var a = control.value
    if (a != '') {
        alert('jetzt gehts weidder!')
    }
    else {
        alert('erst was auswählen!')
    }
}


// kunden-daten

const kundenDatenBox = document.getElementById('kunden-daten-box')
const DDLkunden = document.getElementById('ddlKunden')

$.ajax({
    type: 'GET',
    url: '/kunden-daten/',
    success: function (response) {
        console.log(response.data)
        const kundenDaten = response.data
        kundenDaten.map(item => {
            const option = document.createElement('div')
            const kunde = (item.nachname + ', ' + item.vorname)
            option.textContent = (kunde)
            option.setAttribute('class', 'item')
            option.setAttribute('data-value', item.id)
            kundenDatenBox.appendChild(option)
        })
    },
    error: function (error) {
        console.log(error)
    }
})

DDLkunden.addEventListener('change', e => {
    console.log(e.target.value)
    const selectedKunde = e.target.value
}) 