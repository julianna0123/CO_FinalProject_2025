# Copyright (c) 2012, 2015, 2017 ARM Limited
# All rights reserved.
#
# The license below extends only to copyright in the software and shall
# not be construed as granting a license to any other intellectual
# property including but not limited to intellectual property relating
# to a hardware implementation of the functionality of the software
# licensed hereunder.  You may use the software subject to the license
# terms below provided that you ensure that this notice is replicated
# unmodified and in its entirety in all distributions of the software,
# modified or unmodified, in source code or in binary form.
#
# Copyright (c) 2005-2008 The Regents of The University of Michigan
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Authors: Nathan Binkert
#          Andreas Hansson

from MemObject import MemObject
from System import System
from m5.params import *
from m5.proxy import *
from m5.SimObject import SimObject

class BaseXBar(MemObject):
    type = 'BaseXBar'
    abstract = True
    cxx_header = "mem/xbar.hh"
    slave = VectorSlavePort("Vector port for connecting masters")
    master = VectorMasterPort("Vector port for connecting slaves")

    # Latencies governing the time taken for the variuos paths a
    # packet has through the crossbar. Note that the crossbar itself
    # does not add the latency due to assumptions in the coherency
    # mechanism. Instead the latency is annotated on the packet and
    # left to the neighbouring modules.
    #
    # A request incurs the frontend latency, possibly snoop filter
    # lookup latency, and forward latency. A response incurs the
    # response latency. Frontend latency encompasses arbitration and
    # deciding what to do when a request arrives. the forward latency
    # is the latency involved once a decision is made to forward the
    # request. The response latency, is similar to the forward
    # latency, but for responses rather than requests.
    frontend_latency = Param.Cycles("Frontend latency")
    forward_latency = Param.Cycles("Forward latency")
    response_latency = Param.Cycles("Response latency")

    # Width governing the throughput of the crossbar
    width = Param.Unsigned("Datapath width per port (bytes)")

    # The default port can be left unconnected, or be used to connect
    # a default slave port
    default = MasterPort("Port for connecting an optional default slave")

    # The default port can be used unconditionally, or based on
    # address range, in which case it may overlap with other
    # ports. The default range is always checked first, thus creating
    # a two-level hierarchical lookup. This is useful e.g. for the PCI
    # xbar configuration.
    use_default_range = Param.Bool(False, "Perform address mapping for "
                                   "the default port")


class NoncoherentXBar(BaseXBar):
    type = 'NoncoherentXBar'
    cxx_header = "mem/noncoherent_xbar.hh"


class CoherentXBar(BaseXBar):
    type = 'CoherentXBar'
    cxx_header = "mem/coherent_xbar.hh"
    snoop_response_latency = Param.Cycles("Snoop response latency")
    snoop_filter = Param.SnoopFilter(NULL, "Selected snoop filter")
    point_of_coherency = Param.Bool(False, "Consider this crossbar the "
                                    "point of coherency")
    point_of_unification = Param.Bool(False, "Consider this crossbar the "
                                      "point of unification")

    system = Param.System(Parent.any, "System that the crossbar belongs to.")


class SnoopFilter(SimObject):
    type = 'SnoopFilter'
    cxx_header = "mem/snoop_filter.hh"
    lookup_latency = Param.Cycles(1, "Lookup latency")

    system = Param.System(Parent.any, "System that the crossbar belongs to.")
    max_capacity = Param.MemorySize('8MB', "Maximum capacity of snoop filter")
class L2XBar(CoherentXBar):
    width = 32
    frontend_latency = 1
    forward_latency = 0
    response_latency = 1
    snoop_response_latency = 1
    snoop_filter = SnoopFilter(lookup_latency=0)
    point_of_unification = True


class L3XBar(CoherentXBar):
    width = 32
    frontend_latency = 1
    forward_latency = 0
    response_latency = 1
    snoop_response_latency = 1
    snoop_filter = SnoopFilter(lookup_latency=0)
    point_of_unification = True

class SystemXBar(CoherentXBar):
    width = 16
    frontend_latency = 3
    forward_latency = 4
    response_latency = 2
    snoop_response_latency = 4

    snoop_filter = SnoopFilter(lookup_latency=1)

    point_of_coherency = True

    point_of_unification = True

class IOXBar(NoncoherentXBar):
    width = 16

    frontend_latency = 2
    forward_latency = 1
    response_latency = 2

