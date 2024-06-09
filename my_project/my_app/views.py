from django.http import HttpResponse


def index(request):
    html = '''
    <h1>My first Django application</h1>
    <br><br>
    <p>
    Lorem ipsum dolor sit, amet consectetur adipisicing elit. Deleniti laudantium pariatur quos quidem!
    Eaque officiis nostrum nisi unde ad vel, aut rem beatae atque id officia magni. Molestiae quos
    temporibus cupiditate in fugit, quasi sint consequuntur repellat natus, ipsa tempore veniam! Inventore
    impedit quas quis nihil, praesentium eius mollitia minima, accusamus expedita esse commodi culpa id,
    exercitationem cumque. Temporibus veritatis soluta iure, amet ea ducimus nobis odio dicta quaerat
    corporis at atque iusto perspiciatis laudantium sit, pariatur hic labore inventore cum provident
    architecto illum neque. Vero reiciendis dolorem velit laborum at excepturi aperiam adipisci! Nihil,
    amet. Velit ipsam rem porro, impedit deleniti a? Suscipit natus dolorum vel magnam veniam assumenda
    dolor, esse nesciunt quod tempora cumque et necessitatibus deserunt rerum illum alias eligendi, pariatur
    neque distinctio velit tenetur ab libero maxime modi! Numquam illo quaerat, distinctio deleniti in
    voluptates architecto. Totam sint est perspiciatis, sapiente unde architecto adipisci vitae? Veritatis,
    autem optio. Eos, ab. Fugit quisquam sint minima.
    <br><br>
    Quos modi, quas voluptate in recusandae ut aliquam hic laudantium. Quas sapiente harum blanditiis! Porro
    facere id enim sed similique ullam modi totam ipsa! Iure cumque vitae, eveniet corporis, unde iste
    asperiores atque magni mollitia hic perspiciatis dolores fuga fugiat impedit sapiente. Repellat autem
    expedita officiis sint, dolor asperiores delectus aut reiciendis, voluptatibus nisi voluptates. Tempora
    tenetur hic ad illum fugit quasi a nostrum ducimus ipsam ea exercitationem corrupti excepturi id quos
    aspernatur, blanditiis laboriosam. Saepe minima, exercitationem cumque repudiandae possimus voluptatum
    nemo dolorem incidunt cupiditate nesciunt deserunt corporis? Odit aliquid illo quibusdam omnis enim sint
    nulla suscipit totam pariatur, optio, facilis corrupti fugit iure velit ipsam adipisci debitis,
    praesentium laboriosam dolore culpa? Nemo veritatis eius saepe deserunt dicta, ipsam quos dolorum
    consectetur minima eos commodi delectus qui est quibusdam quod! Ipsa minus eligendi enim, obcaecati nam
    officiis fuga eos maxime ducimus?
    </p>
    <br><br>
    <a href="http://127.0.0.1:8000/about/">About me</a>
    '''
    return HttpResponse(html)


def about(request):
    html = '''
    <h1>About me</h1>
    <br><br>
    <p>
    Lorem ipsum dolor sit, amet consectetur adipisicing elit. Deleniti laudantium pariatur quos quidem!
    Eaque officiis nostrum nisi unde ad vel, aut rem beatae atque id officia magni. Molestiae quos
    temporibus cupiditate in fugit, quasi sint consequuntur repellat natus, ipsa tempore veniam! Inventore
    impedit quas quis nihil, praesentium eius mollitia minima, accusamus expedita esse commodi culpa id,
    exercitationem cumque. Temporibus veritatis soluta iure, amet ea ducimus nobis odio dicta quaerat
    corporis at atque iusto perspiciatis laudantium sit, pariatur hic labore inventore cum provident
    architecto illum neque. Vero reiciendis dolorem velit laborum at excepturi aperiam adipisci! Nihil,
    amet. Velit ipsam rem porro, impedit deleniti a? Suscipit natus dolorum vel magnam veniam assumenda
    dolor, esse nesciunt quod tempora cumque et necessitatibus deserunt rerum illum alias eligendi, pariatur
    neque distinctio velit tenetur ab libero maxime modi! Numquam illo quaerat, distinctio deleniti in
    voluptates architecto. Totam sint est perspiciatis, sapiente unde architecto adipisci vitae? Veritatis,
    autem optio. Eos, ab. Fugit quisquam sint minima.
    </p>
    <br><br>
    <a href="http://127.0.0.1:8000/index/">Return to index</a>
    '''
    return HttpResponse(html)
