import xmlrpclib
import json

class StacksyncServerController():
    """
    Handles requests on objects
    """
    def __init__(self, server_ip, server_port):
        
        #Create Sync server connection
        self.xml_ip = server_ip
        self.xml = server_port
        self.rpc_server = xmlrpclib.ServerProxy("http://"+server_ip+':'+str(server_port))

    def get_metadata(self, user, file_id, include_chunks, version, is_folder):
        version = "null" if version is None else version
        include_chunks = "false" if include_chunks is False else "true"
        file_id = "null" if str(file_id) == "0" else file_id
        is_folder = "false" if is_folder is False else "true"

        response = self.rpc_server.XmlRpcSyncHandler.getMetadata(user, str(file_id), str(include_chunks),
                                                                 str(version), str(is_folder))

        return response

    def get_versions(self, user, file_id):

        response = self.rpc_server.XmlRpcSyncHandler.getVersions(user, str(file_id))
        return response

    def get_folder_contents(self, user, folder_id, include_deleted):
        include_deleted = "true" if include_deleted is True else "false"
        folder_id = "null" if str(folder_id) == '0' else folder_id

        response = self.rpc_server.XmlRpcSyncHandler.getFolderContents(str(user), str(folder_id), str(include_deleted))
        return response

    def delete_item(self, user, file_id, is_folder):
        is_folder = "false" if is_folder is False else "true"

        response = self.rpc_server.XmlRpcSyncHandler.deleteItem(user, str(file_id), str(is_folder))

        return response

    def new_folder(self, user, name, parent):
        parent = "null" if parent is None or str(parent) == "0" else parent

        response = self.rpc_server.XmlRpcSyncHandler.newFolder(str(user), name.encode('utf-8'), str(parent))

        return response

    def new_file(self, user, name, parent, checksum, file_size, mimetype, chunks):
        chunks = [] if chunks is None else chunks
        mimetype = "empty" if mimetype is None else mimetype
        checksum = "0" if checksum is None else checksum
        parent = "null" if parent is None or str(parent) == "0" else parent

        response = self.rpc_server.XmlRpcSyncHandler.newFile(user, name, str(parent),
                                                            str(checksum), str(file_size), str(mimetype), chunks)

        return response

    def update_data(self, user, file_id, checksum, size,  mimetype, chunks):
        chunks = [] if chunks is None else chunks

        response = self.rpc_server.XmlRpcSyncHandler.updateData(user, str(file_id), str(checksum), str(size), str(mimetype), chunks)

        return response

    def update_metadata(self, user, file_id, name, parent):
        parentUpdated = True
        if parent is None:
            parent = "null"
            parentUpdated = False
        elif str(parent) == "0":
            parent = "null"
        
        nameUpdated = True
        if name is None:
            name = "null"
            nameUpdated = False

        response = self.rpc_server.XmlRpcSyncHandler.updateMetadata(str(user), str(file_id), name.encode('utf-8'), str(parent), str(nameUpdated), str(parentUpdated))

        return response

    def get_workspace_info(self, user, item_id):
        item_id = "null" if item_id is None or str(item_id) == "0" else item_id
        
        response = self.rpc_server.XmlRpcSyncHandler.getWorkspaceInfo(str(user), str(item_id))
        return response

    def share_folder(self, user_id, folder_id, users_list):
        message = self.rpc_server.XmlRpcSyncHandler.shareFolder(str(user_id), str(folder_id), users_list)
        return message

    def unshare_folder(self, user_id, folder_id, users_list):
        message = self.rpc_server.XmlRpcSyncHandler.unshareFolder(str(user_id), str(folder_id), users_list)
        return message

    def get_folder_members(self, user_id, folder_id):
        message = self.rpc_server.XmlRpcSyncHandler.getFolderMembers(str(user_id), str(folder_id))
        return message
