function getData()
{
    fetch("http://127.0.0.1:8000/raktar/getdata").then(response=>response.json()).then(result=>
    {
        result.forEach(x =>
        {
            document.querySelector("#termekek").innerHTML+=
            `
            <tr>
            <td>${x.termekNev}</td>
            <td>${x.ar}</td>
            <td>${x.db}</td>
            <td>${x.kategoria.kategoriaNev}</td>
            </tr>
            `;
        });
    });
}

getData();