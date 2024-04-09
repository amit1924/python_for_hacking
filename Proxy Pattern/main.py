#  the Proxy Design Pattern can be used for various purposes, such as delaying object creation, controlling access, logging, or monitoring.

from abc import ABC, abstractmethod
from datetime import datetime


class Subject(ABC):
    @abstractmethod
    def request(self):
        pass


class RealSubject(Subject):
    def request(self):
        print("RealSubject:Handling request")


class Proxy(Subject):
    def __init__(self):
        self.real_subject = RealSubject()

    def request(self):
        print(f"Proxy : Logging{datetime.now()}")
        self.real_subject.request()


proxy = Proxy()
print(proxy.request())
