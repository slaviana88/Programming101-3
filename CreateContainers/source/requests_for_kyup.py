CLOUD_CREATE = """request={"action":"cloudCreate",
                            "authorization_key":"2bcb447b43f0e1a2b9a19fae24a2ae9e87",
                            "data":{"name":"%s",
                                    "password":"tester12345",
                                    "image_name":"Ubuntu Trusty 14.04",
                                    "datacenter_id":1,
                                    "resources":
                                                {"mem":2,"hdd":40,"cpu":2,"bw":2}}}"""

CLOUD_DETAILS = """request={"action":"cloudDetails",
                            "authorization_key":"2bcb447b43f0e1a2b9a19fae24a2ae9e87",
                            "data":{"container_id":%s}}"""

ADD_SSH_KEY = """request={"action":"sshAddKey",
                          "authorization_key":"2bcb447b43f0e1a2b9a19fae24a2ae9e87",
                          "data":{"key":"%s","title":"%s"}}"""

INSTALL_SSH_KEY = """request={"action":"sshInstallKey",
                              "authorization_key":"2bcb447b43f0e1a2b9a19fae24a2ae9e87",
                              "data":{"key_id":%s,
                                      "container_id":%s}}"""

CLOUD_LIST = """request={"action":"cloudList",
                                 "authorization_key":"2bcb447b43f0e1a2b9a19fae24a2ae9e87",
                                 "data" : {}}"""


GET_TASK = """request={"action":"getTask",
                        "authorization_key":"2bcb447b43f0e1a2b9a19fae24a2ae9e87",
                        "data":{
                        "task_id":%s}}"""
