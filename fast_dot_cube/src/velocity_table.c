#include "genesis.h"
#include "../../src/velocity_table.h"

const s8 vel_table[VEL_TABLE_LEN][VEL_TABLE_LEN] = {
	{ 0, 0, 1, 1, 2, 3, 3, 3, },

	{ 0, 0, 0, 1, 2, 3, 3, 4, },

	{ 6, 0, 0, 1, 2, 3, 4, 4, },

	{ 6, 6, 6, 0, 2, 4, 5, 5, },

	{ 6, 6, 6, 6, 2, 6, 6, 6, },

	{ 6, 6, 6, 0, 2, 4, 5, 5, },

	{ 6, 0, 0, 1, 2, 3, 4, 4, },

	{ 0, 0, 0, 1, 2, 3, 3, 4, },
};
