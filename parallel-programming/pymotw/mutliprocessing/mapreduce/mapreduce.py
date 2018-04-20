import collections
import itertools
import multiprocessing


class SimpleMapReduce:
    def __init__(self, map_func, reduce_func, num_workers=None ):
        self.map_func = map_func
        self.reduce_func = reduce_func
        self.pool = multiprocessing.Pool(num_workers)


    def partition(self, mapped_values):
        partitioned_data = collections.defaultdict(list)
        for k,v in mapped_values:
            partitioned_data[k].append(v)

        return partitioned_data.items()

    def __call__(self, inputs, chunksize=1):
        map_responese = self.pool.map(
            self.map_func,
            inputs,
            chunksize=chunksize,
        )

        partitioned_data = self.partition(
            itertools.chain(*map_responese)
        )

        reduced_values = self.pool.map(
            self.reduce_func,
            partitioned_data,
        )
        
        return reduced_values



