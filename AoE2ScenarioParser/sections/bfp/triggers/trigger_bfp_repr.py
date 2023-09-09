from io import StringIO

from binary_file_parser import BaseStruct
from binary_file_parser.retrievers import Retriever
from binary_file_parser.utils import indentify


class TriggerBfpRepr:

    def __repr__(self):
        repr_builder = StringIO()
        repr_builder.write(f"{self.__class__.__name__}(")

        content_repr = StringIO()

        # Direct children shouldn't make use of refs
        bases = type(self).__bases__
        is_direct_child = len(bases) > 1 and bases[1] is BaseStruct

        if is_direct_child and not self._refs:
            get_ = lambda retriever: (retriever, retriever.p_name)
            list_ = self._retrievers
        else:
            get_ = lambda ref: (ref.retriever, ref.name)
            list_ = self._refs

        for retriever in list_:
            self._retriever_as_string(*get_(retriever), builder = content_repr)

        if content := content_repr.getvalue():
            repr_builder.write(f"{content}\n")

        repr_builder.write(")")
        return repr_builder.getvalue()

    def _retriever_as_string(self, retriever: Retriever, name: str, builder: StringIO):
        if not retriever.supported(self.struct_ver):
            return

        obj = getattr(self, retriever.p_name)
        if isinstance(obj, list):
            if len(obj) == 0:
                sub_obj_repr_str = '[]'
            else:
                sub_obj_repr_str = '\n'.join((
                    "[",
                    "\t" + ",\n\t".join(map(lambda x: indentify(repr(x)), obj)),
                    "]"
                ))
        else:
            sub_obj_repr_str = f"{obj!r}"

        builder.write(f"\n    {name} = {indentify(sub_obj_repr_str)},")
