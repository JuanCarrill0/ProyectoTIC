package tutorial.misionTIC.ModuloSeguridad.Repositorios;

import org.springframework.data.mongodb.repository.MongoRepository;
import tutorial.misionTIC.ModuloSeguridad.Modelos.PermisosRoles;
import org.springframework.data.mongodb.repository.Query;

public interface RepositorioPermisosRoles extends MongoRepository<PermisosRoles,String> {
    @Query("{'rol.$id': ObjectId(?0),'permiso.$id': ObjectId(?1)}")
    PermisosRoles getPermisoRol(String id_rol,String id_permiso);
<<<<<<< HEAD
}
=======
}
>>>>>>> 557885340c0a4f2d3e7a9e16627610c935c942a7
